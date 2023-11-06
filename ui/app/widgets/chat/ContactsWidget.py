from managers.RegexManager import RegexManager
from .Scrollarea import Scrollarea
from PyQt6 import QtGui
from PyQt6.QtWidgets import QLineEdit, QWidget

class ContactsWidget(QWidget):

    def __init__(self, parent: QWidget) -> None:
        
        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        super().__init__(parent)

        self.__contacts_search = self.__get_contacts_search()
        self.__contacts_scrollarea = Scrollarea(self, self.__contacts_scrollarea_enter_event, self.__contacts_scrollarea_leave_event)
        
        self.__contacts_scrollarea.verticalScrollBar().setObjectName("contactsScrollbarHidden")

    @property
    def contacts_search(self) -> QLineEdit:
        return self.__contacts_search
    
    @property
    def contacts_scrollarea(self) -> Scrollarea:
        return self.__contacts_scrollarea
    
    def add_contact(self, contact: QWidget) -> None:

        if not isinstance(contact, QWidget):
            raise TypeError(type(contact)) 

        self.__contacts_scrollarea.add_widget(contact)

    def __get_contacts_search(self) -> QLineEdit:
                
        contacts_search = QLineEdit(self)

        line_edit_validator = RegexManager.get_regex_nickname_validator()

        placeholder_palette = contacts_search.palette()
        placeholder_palette.setColor(QtGui.QPalette.ColorRole.PlaceholderText, QtGui.QColor("#555555"))  

        contacts_search.setPalette(placeholder_palette)
        contacts_search.setValidator(line_edit_validator)
        contacts_search.setPlaceholderText("Search")
        contacts_search.setObjectName("contactsSearch")

        return contacts_search
    
    def __contacts_scrollarea_enter_event(self) -> None:

        self.__contacts_scrollarea.verticalScrollBar().setObjectName("contactsScrollbarShowed")
        self.__contacts_scrollarea.setStyleSheet(self.__contacts_scrollarea.styleSheet())

    def __contacts_scrollarea_leave_event(self) -> None:

        self.__contacts_scrollarea.verticalScrollBar().setObjectName("contactsScrollbarHidden")
        self.__contacts_scrollarea.setStyleSheet(self.__contacts_scrollarea.styleSheet())