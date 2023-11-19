from .Contact import Contact
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class MessagesWidget(QWidget):

    def __init__(self) -> None:

        super().__init__()

        self.__contact = None

        self.__layout = QVBoxLayout()

    @property
    def layout(self) -> QVBoxLayout:
        return self.__layout

    @property
    def contact(self) -> Contact:
        return self.__contact
    
    @contact.setter
    def contact(self, contact: Contact) -> Contact:

        if not isinstance(contact, Contact):
            raise TypeError(type(contact))

        self.__contact = contact

    def hide_contact_dialog(self) -> None:

        for _ in range(self.__layout.count()): 
            self.__layout.itemAt(0).widget().setParent(None)

    def show_contact_dialog(self, contact: Contact) -> None:

        if not isinstance(contact, Contact):
            raise TypeError(type(contact))

        currentContactName = QLabel(contact.text())

        currentContactName.setObjectName("currentContactName")

        self.__layout.addWidget(currentContactName)
        self.__layout.addWidget(contact.messages_scrollarea)
        self.__layout.addWidget(contact.message_edit)
