from typing import Callable
from PyQt6 import QtCore
from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtGui import QMouseEvent

class Contact(QLabel):
    
    def __init__(self, parent: QWidget, id: int, name: str, contact_selected_callback: Callable[['Contact'], None]) -> None:
        
        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        if not isinstance(id, int):
            raise TypeError(type(id))

        if not isinstance(name, str):
            raise TypeError(name)
        
        if not isinstance(contact_selected_callback, Callable):
            raise TypeError(contact_selected_callback)

        super().__init__(name, parent)

        self.__id = id
        self.__contact_selected_callback = contact_selected_callback

        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

    @property
    def id(self) -> int:
        return self.__id

    def mousePressEvent(self, event: QMouseEvent | None) -> None:

        super().mousePressEvent(event)

        self.__contact_selected_callback(self)

        self.setObjectName("selected")
        self.setStyleSheet("")
    