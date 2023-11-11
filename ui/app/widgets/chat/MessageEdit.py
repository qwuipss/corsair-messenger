from typing import Callable 
from ...SharedQSS import SharedQSS
from PyQt6.QtWidgets import QTextEdit, QWidget
from PyQt6 import QtCore
from PyQt6 import QtGui

class MessageEdit(QTextEdit):

    def __init__(self, parent: QWidget, max_height: int, message_sent_callback: Callable[[], str]):

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        if not isinstance(max_height, int):
            raise TypeError(type(max_height))

        if not isinstance(message_sent_callback, Callable):
            raise TypeError(type(message_sent_callback))

        super().__init__(parent)

        self.__max_height = max_height
        self.__message_sent_callback = message_sent_callback

        placeholder_palette = self.palette()
        placeholder_palette.setColor(QtGui.QPalette.ColorRole.PlaceholderText, QtGui.QColor(f"#{SharedQSS.COLOR_555555}"))  

        self.textChanged.connect(self.__adjust_height)
        self.setPalette(placeholder_palette)
        self.setPlaceholderText("Write a message...")
        self.installEventFilter(self)

    def eventFilter(self, object: QtCore.QObject | None, event: QtCore.QEvent | None) -> bool:

        super().eventFilter(object, event)

        if object is self:
            
            if self.hasFocus():
                
                if event.type() == QtCore.QEvent.Type.KeyPress:
                    
                    if event.key() == QtCore.Qt.Key.Key_Return and event.modifiers() != QtCore.Qt.KeyboardModifier.ShiftModifier:
                        
                        text = self.toPlainText()
                        
                        if not str.isspace(text) and text != "":
                            self.__message_sent_callback(text)
                        
                        self.setPlainText("")
                        
                        return True
            
        return False
    
    def resizeEvent(self, event: QtCore.QEvent | None) -> None:

        super().resizeEvent(event)

        self.__adjust_height()

    def __adjust_height(self) -> None:

        document_height = int(self.document().size().height())
        paddings = self.contentsMargins()

        if document_height <= self.__max_height:
            self.setFixedHeight(document_height + paddings.top() + paddings.bottom())
