from typing import Callable
from PyQt6 import QtCore
from PyQt6.QtGui import QEnterEvent, QMouseEvent
from PyQt6.QtWidgets import QLabel

class LastMessage(QLabel):
    
    def __init__(
            self, 
            text: str, 
            hovered_callback: Callable[[], None],
            unhovered_callback: Callable[[], None], 
            selected_callback: Callable[[], None]
            ):

        if not isinstance(text, str):
            raise TypeError(type(text))

        if not isinstance(hovered_callback, Callable):
            raise TypeError(type(hovered_callback))
        
        if not isinstance(unhovered_callback, Callable):
            raise TypeError(type(unhovered_callback))
        
        if not isinstance(selected_callback, Callable):
            raise TypeError(type(selected_callback))
        
        super().__init__(text)

        self.__hovered_callback = hovered_callback
        self.__unhovered_callback = unhovered_callback

        self.__selected_callback = selected_callback

        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

    def enterEvent(self, event: QEnterEvent | None) -> None:
        
        super().enterEvent(event)

        self.__hovered_callback()

    def leaveEvent(self, event: QtCore.QEvent | None) -> None:
        
        super().leaveEvent(event)

        self.__unhovered_callback()

    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        
        super().mousePressEvent(event)

        self.__selected_callback()