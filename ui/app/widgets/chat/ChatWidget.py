from .ContactsWidget import ContactsWidget
from .MessagesWidget import MessagesWidget
from .ChatWidgetQSS import ChatWidgetQSS
from .Contact import Contact
from .Message import Message
from client.Client import Client
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QMainWindow, QLabel

class ChatWidget(QWidget):

    def __init__(self, main_window: QMainWindow, client: Client) -> None:

        if not isinstance(main_window, QWidget):
            raise TypeError(type(main_window))
        
        if not isinstance(client, Client):
            raise TypeError(type(client))

        super().__init__()

        self.__client = client
        
        self.__contacts_widget = ContactsWidget()
        self.__messages_widget = MessagesWidget()

        self.__messages_layout = self.__get_messages_layout()

        self.setLayout(self.__get_main_layout())
        self.setStyleSheet(ChatWidgetQSS(main_window).qss)

        self.__load_contacts(main_window)
        client.start_receiving(self.__message_received_callback)

    def __get_main_layout(self) -> QHBoxLayout:

        layout = QHBoxLayout()

        contacts_layout = self.__get_contacts_layout()

        layout.addLayout(contacts_layout, 2)
        layout.addLayout(self.__messages_layout, 5)

        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        return layout

    def __get_contacts_layout(self) -> QVBoxLayout:

        contacts_layout = QVBoxLayout()

        contacts_layout.addWidget(self.__contacts_widget.contacts_search)
        contacts_layout.addWidget(self.__contacts_widget.contacts_scrollarea)

        return contacts_layout
    
    def __get_messages_layout(self) -> QVBoxLayout:

        messages_layout = QVBoxLayout()

        return messages_layout
    
    def __load_contacts(self, main_window: QMainWindow) -> None:

        contacts = self.__client.get_contacts()

        for raw_contact in contacts:

            contact = Contact(
                int(raw_contact["id"]), 
                raw_contact["nickname"], 
                self.__contact_selected_callback, 
                self.__message_sent_callback, 
                self.__client.pull_messages, 
                main_window
                )

            self.__contacts_widget.add_contact(contact)

    def __contact_selected_callback(self, contact: Contact) -> None:

        if not isinstance(contact, Contact):
            raise TypeError(type(contact))
        
        self.__hide_contact_dialog()
        self.__show_contact_dialog(contact)

        previous_contact = self.__messages_widget.contact
        self.__messages_widget.contact = contact

        if previous_contact is None:
            return

        previous_contact.setObjectName("") 
        previous_contact.setStyleSheet("") 

    def __message_sent_callback(self, receiver_id: int, text: str) -> None:
        
        if not isinstance(receiver_id, int):
            raise TypeError(type(receiver_id))
        
        if not isinstance(text, str):
            raise TypeError(type(text))

        self.__client.send_message(receiver_id=receiver_id, text=text)

    def __hide_contact_dialog(self) -> None:

        for i in range(self.__messages_layout.count()): 
            self.__messages_layout.itemAt(0).widget().setParent(None)

    def __show_contact_dialog(self, contact: Contact) -> None:

        if not isinstance(contact, Contact):
            raise TypeError(type(contact))

        currentContactName = QLabel(contact.text())

        currentContactName.setObjectName("currentContactName")

        self.__messages_layout.addWidget(currentContactName)
        self.__messages_layout.addWidget(contact.messages_scrollarea)
        self.__messages_layout.addWidget(contact.message_edit)

    def __message_received_callback(self, raw_message: dict) -> None:

        message_id = raw_message["id"]
        sender_id = int(raw_message["sender_id"])

        receiver = self.__contacts_widget.contacts[sender_id]

        message = Message(message_id, raw_message["text"])

        receiver.add_message(message, sender_id != receiver.id)
