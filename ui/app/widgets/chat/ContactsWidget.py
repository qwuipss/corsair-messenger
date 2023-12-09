from .ContactsSearch import ContactsSearch
from .Scrollarea import Scrollarea
from .Contact import Contact
from typing import Callable
from PyQt6.QtWidgets import QLineEdit, QWidget, QVBoxLayout
from client.Client import Client
from PyQt6 import QtCore

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

        self.__contacts_search = ContactsSearch(contacts_search_requested_delegate, self.show_contacts)
        self.__contacts_scrollarea = Scrollarea("contactsScrollbarShowed", "contactsScrollbarHidden")

        self.__searched_contacts_layouts_list = []

        self.search_view_active = False

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

    def show_searched_contacts(self) -> None:

        self.__clear_contacts_scrollarea()

        self.__fill_contacts_scrollarea(self.__searched_contacts_layouts_list)

    def show_contacts(self) -> None:
        
        self.remove_searched_contacts_if_needed()
        self.__clear_contacts_scrollarea()
        
        self.search_view_active = False

        contacts_layouts = []

        for contact in self.__contacts.values():

            contact_layout = self.__create_contact_layout(contact)

            contacts_layouts.append(contact_layout)

        self.__fill_contacts_scrollarea(contacts_layouts)

        if self.__contacts_scrollarea.widget().underMouse():
            self.__contacts_scrollarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)

    def add_and_show_contact(self, contact: Contact) -> None:

        if not isinstance(contact, Contact):
            raise TypeError(type(contact))      

        self.add_contact(contact)

        contact_layout = self.__create_contact_layout(contact)

        self.__contacts_scrollarea.layout.insertLayout(self.__contacts_scrollarea.layout.count() - 1, contact_layout)

    def add_contact(self, contact: Contact) -> None:

        if not isinstance(contact, Contact):
            raise TypeError(type(contact))      

        self.__contacts.update({contact.id : contact})
    
    def add_searched_contact(self, contact: Contact) -> None:

        if not isinstance(contact, Contact):
            raise TypeError(type(contact))      

        contact_layout = self.__create_contact_layout(contact)

        self.__searched_contacts_layouts_list.append(contact_layout)

        self.__contacts.update({contact.id : contact})

    def __create_contact_layout(self, contact: Contact) -> QVBoxLayout:

        if not isinstance(contact, Contact):
            raise TypeError(type(contact))  

        contact_layout = QVBoxLayout()

        contact_layout.setSpacing(0)

        contact.setContentsMargins(0, 0, 0, 0)
        contact.last_message_label.setContentsMargins(0, 0, 0, 0)

        contact_layout.addWidget(contact)
        contact_layout.addWidget(contact.last_message_label)

        return contact_layout

    def __load_contacts_on_scrollbar_down(self) -> None:
        
        scrollbar = self.__contacts_scrollarea.verticalScrollBar()

        value = scrollbar.value()

        if value == scrollbar.maximum():
            self.__contacts_load_requested_delegate()
            self.__contacts_loading_offset += Client.CONTACTS_AFTER_LOAD_COUNT
            self.__scrollbar_value_before_add_new_contacts = value

    def __return_scrollbar_on_position_before_loading_contacts(self) -> None:
        
        self.__contacts_scrollarea.verticalScrollBar().setValue(self.__scrollbar_value_before_add_new_contacts)

    def __fill_contacts_scrollarea(self, contacts_layouts: list) -> None:

        if not isinstance(contacts_layouts, list):
            raise TypeError(type(contacts_layouts))          

        for contact_layout in contacts_layouts:
            self.__contacts_scrollarea.layout.insertLayout(self.__contacts_scrollarea.layout.count() - 1, contact_layout)

    def __clear_contacts_scrollarea(self) -> None:

        if self.__contacts_scrollarea.layout.count() == 1:
            return

        for _ in range(self.__contacts_scrollarea.layout.count() - 1):
            
            contact_layout = self.__contacts_scrollarea.layout.takeAt(0)
            
            for _ in range(contact_layout.count()):

                widget = contact_layout.takeAt(0).widget()

                widget.setParent(None)

    def remove_searched_contacts_if_needed(self) -> None:

        if len(self.__searched_contacts_layouts_list) != 0:

            for contact_layout in self.__searched_contacts_layouts_list:

                contact = contact_layout.itemAt(0).widget()

                if contact.has_messages: 
                    self.__contacts.pop(contact.id)

            self.__searched_contacts_layouts_list.clear()
