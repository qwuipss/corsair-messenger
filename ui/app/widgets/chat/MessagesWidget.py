from .Contact import Contact
from PyQt6.QtWidgets import QWidget

class MessagesWidget(QWidget):

    def __init__(self) -> None:

        super().__init__()

        self.__contact = None

    @property
    def contact(self) -> Contact:
        return self.__contact
    
    @contact.setter
    def contact(self, contact: Contact) -> Contact:

        if not isinstance(contact, Contact):
            raise TypeError(type(contact))

        self.__contact = contact
