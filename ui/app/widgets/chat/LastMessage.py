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
            ) -> None:

        if not isinstance(text, str):
            raise TypeError(type(text))

        if not isinstance(hovered_callback, Callable):
            raise TypeError(type(hovered_callback))
        
        if not isinstance(unhovered_callback, Callable):
            raise TypeError(type(unhovered_callback))
        
        if not isinstance(selected_callback, Callable):
            raise TypeError(type(selected_callback))
        
        super().__init__()

        self.__font_metrics = self.fontMetrics()
        self.__text_width = int(self.width() * 0.45)

        self.setText(text)

        self.__hovered_callback = hovered_callback
        self.__unhovered_callback = unhovered_callback

        self.__selected_callback = selected_callback

        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

    def setText(self, text: str | None) -> None:
        
        remain_width = self.__text_width

        chars_count = 0
        is_limit_exceeded = False

        for char in text:

            remain_width -= self.__font_metrics.horizontalAdvance(char) * 1.1
            
            if remain_width > 0:
                chars_count += 1
            else:
                is_limit_exceeded = True
                break

        if is_limit_exceeded:
            text_continuing = "..."
            super().setText(text[:chars_count - len(text_continuing)] + text_continuing)
        else:
            super().setText(text)

    def enterEvent(self, event: QEnterEvent | None) -> None:
        
        super().enterEvent(event)

        self.__hovered_callback()

    def leaveEvent(self, event: QtCore.QEvent | None) -> None:
        
        super().leaveEvent(event)

        self.__unhovered_callback()

    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        
        super().mousePressEvent(event)

        self.__selected_callback()