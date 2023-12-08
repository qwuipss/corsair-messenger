from .ContactsSearch import ContactsSearch
from .Scrollarea import Scrollarea
from .Contact import Contact
from typing import Callable
from PyQt6.QtWidgets import QLineEdit, QWidget, QVBoxLayout
from client.Client import Client

class ContactsWidget(QWidget):

    def __init__(
            self, 
            contacts_search_requested_delegate: Callable[[str], None], 
            contacts_load_requested_delegate: Callable[[], None]
            ) -> None:
        
        if not isinstance(contacts_search_requested_delegate, Callable):
            raise TypeError(type(contacts_search_requested_delegate))
        
        if not isinstance(contacts_load_requested_delegate, Callable):
            raise TypeError(type(contacts_load_requested_delegate))

        super().__init__()

        self.__contacts_loading_offset = 0
        self.__contacts = {}

        self.__scrollbar_value_before_add_new_contacts = 0

        self.__contacts_search = ContactsSearch(contacts_search_requested_delegate)
        self.__contacts_scrollarea = Scrollarea("contactsScrollbarShowed", "contactsScrollbarHidden")

        self.__contacts_load_requested_delegate = contacts_load_requested_delegate

        self.__contacts_scrollarea.widget().setObjectName("contactsScrollwidget")

        self.__contacts_scrollarea.layout.addStretch(1)
        self.__contacts_scrollarea.layout.setSpacing(0)
        self.__contacts_scrollarea.layout.setContentsMargins(0, 0, 0, 0)

        self.__contacts_scrollarea.verticalScrollBar().valueChanged.connect(self.__load_contacts_on_scrollbar_down)
        self.__contacts_scrollarea.verticalScrollBar().rangeChanged.connect(self.__return_scrollbar_on_position_before_loading_contacts)

    @property
    def contacts_loading_offset(self) -> int:
        return self.__contacts_loading_offset
    
    @contacts_loading_offset.setter
    def contacts_loading_offset(self, value: int) -> None:

        if not isinstance(value, int):
            raise TypeError(type(value))
        
        if value < 0:
            raise ValueError(value) 

        self.__contacts_loading_offset = value

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

        if not isinstance(contact, Contact):
            raise TypeError(type(contact))      

        contact_layout = QVBoxLayout()

        contact_layout.setSpacing(0)

        contact.setContentsMargins(0,0,0,0)
        contact.last_message_label.setContentsMargins(0,0,0,0)

        contact_layout.addWidget(contact)
        contact_layout.addWidget(contact.last_message_label)

        contacts_count = self.__contacts_scrollarea.layout.count()

        if contacts_count > 1:
            self.__contacts_scrollarea.layout.insertLayout(contacts_count - 1, contact_layout)
        else:
            self.__contacts_scrollarea.layout.insertLayout(0, contact_layout)

        self.__contacts.update({contact.id : contact})

    def __load_contacts_on_scrollbar_down(self) -> None:
        
        scrollbar = self.__contacts_scrollarea.verticalScrollBar()

        value = scrollbar.value()

        if value == scrollbar.maximum():
            self.__contacts_load_requested_delegate()
            self.__contacts_loading_offset += Client.CONTACTS_AFTER_LOAD_COUNT
            self.__scrollbar_value_before_add_new_contacts = value

    def __return_scrollbar_on_position_before_loading_contacts(self) -> None:
        
        self.__contacts_scrollarea.verticalScrollBar().setValue(self.__scrollbar_value_before_add_new_contacts)