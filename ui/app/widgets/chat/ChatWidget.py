import asyncio
from .ContactsWidget import ContactsWidget
from .MessagesWidget import MessagesWidget
from .ChatWidgetQSS import ChatWidgetQSS
from .Message import Message
from client.Client import Client
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QWidget, QMainWindow
from events import Events

class ChatWidget(QWidget):

    def __init__(self, main_window: QMainWindow, client: Client) -> None:

        if not isinstance(main_window, QWidget):
            raise TypeError(type(main_window))
        
        if not isinstance(client, Client):
            raise TypeError(type(client))

        super().__init__(main_window)

        self.__client = client
        
        self.__contacts_widget = ContactsWidget(self)
        self.__messages_widget = MessagesWidget(main_window, self, self.__client.send_message)

        # ---------------
        for i in range(15):

            contact_label = QLabel(f"contact{i}")
            self.__contacts_widget.add_contact(contact_label)

            message = Message("hello world", self)
            self.__messages_widget.add_message(message, i % 2 == 0)
            message = Message("how are you", self)
            self.__messages_widget.add_message(message, i % 2 == 0)
            message = Message("good job", self)
            self.__messages_widget.add_message(message, i % 2 == 1)
            message = Message("yeah it is", self)
            self.__messages_widget.add_message(message, i % 2 == 1)
        # -------------

        layout = self.__get_main_layout()

        self.setLayout(layout)
        self.setStyleSheet(ChatWidgetQSS(main_window).qss)

        client.start_receiving()

    def __get_main_layout(self) -> QHBoxLayout:

        layout = QHBoxLayout()

        contacts_layout = self.__get_contacts_layout()
        messages_layout = self.__get_messages_layout()

        layout.addLayout(contacts_layout, 2)
        layout.addLayout(messages_layout, 5)

        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        return layout

    def __get_contacts_layout(self) -> QVBoxLayout:

        contacts_layout = QVBoxLayout()

        self.__contacts_widget.contacts_scrollarea.layout.setSpacing(0)
        self.__contacts_widget.contacts_scrollarea.layout.setContentsMargins(0, 0, 0, 0)

        contacts_layout.addWidget(self.__contacts_widget.contacts_search)
        contacts_layout.addWidget(self.__contacts_widget.contacts_scrollarea)

        return contacts_layout
    
    def __get_messages_layout(self) -> QVBoxLayout:

        messages_layout = QVBoxLayout()
        
        messages_layout.addWidget(self.__messages_widget.current_contact_name)
        messages_layout.addWidget(self.__messages_widget.messages_scrollarea)
        messages_layout.addWidget(self.__messages_widget.message_edit)

        return messages_layout
    