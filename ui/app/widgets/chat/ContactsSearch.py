from ...SharedQSS import SharedQSS
from managers.RegexManager import RegexManager
from typing import Callable
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QLineEdit

class ContactsSearch(QLineEdit):

    def __init__(self, search_requested_delegate: Callable[[str], None], search_aborted_delegate: Callable[[], None]) -> None:
        
        if not isinstance(search_requested_delegate, Callable):
            raise TypeError(type(search_requested_delegate))

        super().__init__()

        self.__search_requested_delegate = search_requested_delegate
        self.__search_aborted_delegate = search_aborted_delegate

        line_edit_validator = RegexManager.get_regex_nickname_validator()

        placeholder_palette = self.palette()
        placeholder_palette.setColor(QtGui.QPalette.ColorRole.PlaceholderText, QtGui.QColor(f"#{SharedQSS.COLOR_555555}"))  

        self.__previous_search_text = ""
        self.__last_search_request_text_length = 0
        self.__need_search_aborting = False

        self.textChanged.connect(self.__text_changed_handler)

        self.setPalette(placeholder_palette)
        self.setPlaceholderText("Search")
        self.setValidator(line_edit_validator)
        self.setObjectName("contactsSearch")

    def keyPressEvent(self, event: QtGui.QKeyEvent | None) -> None:
        
        super().keyPressEvent(event)

        if event.key() == QtCore.Qt.Key.Key_Return:
            
            text = self.text()

            if not str.isspace(text) and text and self.__previous_search_text != text:
                self.__search_requested_delegate(text)
                self.__last_search_request_text_length = len(text)
                self.__need_search_aborting = True
                self.__previous_search_text = text

    def __text_changed_handler(self) -> None:

        text_length = len(self.text())

        if text_length < self.__last_search_request_text_length and self.__need_search_aborting:
            self.__need_search_aborting = False
            self.__search_aborted_delegate()
            self.__previous_search_text = ""
