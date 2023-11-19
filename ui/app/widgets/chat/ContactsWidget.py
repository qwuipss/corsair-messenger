from .ContactsSearch import ContactsSearch
from .Scrollarea import Scrollarea
from .Contact import Contact
from typing import Callable
from PyQt6.QtWidgets import QLineEdit, QWidget

class ContactsWidget(QWidget):

    def __init__(self, contacts_search_requested_delegate: Callable[[str], None]) -> None:
        
        super().__init__()

        self.__contacts_loading_offset = 0
        self.__contacts = {}

        self.__contacts_search = ContactsSearch(contacts_search_requested_delegate)
        self.__contacts_scrollarea = Scrollarea()

        self.__contacts_scrollarea.widget().setObjectName("contactsScrollwidget")

        self.__contacts_scrollarea.layout.addStretch(1)
        self.__contacts_scrollarea.layout.setSpacing(0)
        self.__contacts_scrollarea.layout.setContentsMargins(0, 0, 0, 0)

    @property
    def contacts_loading_offset(self) -> int:
        return self.__contacts_loading_offset

    @property
    def contacts_search(self) -> QLineEdit:
        return self.__contacts_search
    
    @property
    def contacts_scrollarea(self) -> Scrollarea:
        return self.__contacts_scrollarea
     
    @property
    def contacts(self) -> dict:
        return self.__contacts

    def add_contact(self, contact: Contact) -> None:

        if not isinstance(contact, QWidget):
            raise TypeError(type(contact)) 

        self.__contacts_scrollarea.layout.insertWidget(0, contact)

        self.__contacts.update({contact.id : contact})

    def __load_contacts_on_scrollbar_down(self) -> None:
        pass
