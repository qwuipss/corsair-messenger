from ...SharedQSS import SharedQSS
from managers.RegexManager import RegexManager
from typing import Callable
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QLineEdit

class ContactsSearch(QLineEdit):

    def __init__(self, search_requested_delegate: Callable[[str], None]) -> None:
        
        if not isinstance(search_requested_delegate, Callable):
            raise TypeError(type(search_requested_delegate))

        super().__init__()

        self.__search_requested_delegate = search_requested_delegate

        line_edit_validator = RegexManager.get_regex_nickname_validator()

        placeholder_palette = self.palette()
        placeholder_palette.setColor(QtGui.QPalette.ColorRole.PlaceholderText, QtGui.QColor(f"#{SharedQSS.COLOR_555555}"))  

        self.setPalette(placeholder_palette)
        self.setPlaceholderText("Search")
        self.setValidator(line_edit_validator)
        self.setObjectName("contactsSearch")

    def keyPressEvent(self, event: QtGui.QKeyEvent | None) -> None:
        
        super().keyPressEvent(event)

        if event.key() == QtCore.Qt.Key.Key_Return:
            self.__search_requested_delegate(self.text())
