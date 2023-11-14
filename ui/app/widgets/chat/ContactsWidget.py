from managers.RegexManager import RegexManager
from ...SharedQSS import SharedQSS
from .Scrollarea import Scrollarea
from .Contact import Contact
from PyQt6 import QtGui
from PyQt6.QtWidgets import QLineEdit, QWidget

class ContactsWidget(QWidget):

    def __init__(self) -> None:
        
        super().__init__()

        self.__contacts = {}

        self.__contacts_search = self.__get_contacts_search()
        self.__contacts_scrollarea = Scrollarea()
        
        self.__contacts_scrollarea.layout.addStretch(1)
        self.__contacts_scrollarea.layout.setSpacing(0)
        self.__contacts_scrollarea.layout.setContentsMargins(0, 0, 0, 0)

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

    def __get_contacts_search(self) -> QLineEdit:
                
        contacts_search = QLineEdit(self)

        line_edit_validator = RegexManager.get_regex_nickname_validator()

        placeholder_palette = contacts_search.palette()
        placeholder_palette.setColor(QtGui.QPalette.ColorRole.PlaceholderText, QtGui.QColor(f"#{SharedQSS.COLOR_555555}"))  

        contacts_search.setPalette(placeholder_palette)
        contacts_search.setPlaceholderText("Search")
        contacts_search.setValidator(line_edit_validator)
        contacts_search.setObjectName("contactsSearch")

        return contacts_search
    