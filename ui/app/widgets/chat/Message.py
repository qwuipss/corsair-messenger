from PyQt6.QtWidgets import QWidget, QTextEdit
from PyQt6.QtGui import QTextOption, QResizeEvent
from PyQt6.QtCore import QRect
from math import ceil

class Message(QTextEdit):
    
    def __init__(self, text: str, parent: QWidget):

        if not isinstance(text, str):
            raise TypeError(type(text))
        
        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        super().__init__(parent)

        self.setWordWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
        
        self.textChanged.connect(self.__adjust_height)

        self.setText(text)
        self.setReadOnly(True)

    def resizeEvent(self, _: QResizeEvent) -> None:

        self.__adjust_height()
        
    def __adjust_height(self) -> None:
        
        viewport_width = self.viewport().width()
        self.document().setTextWidth(viewport_width)

        a = self.document().idealWidth() + self.document().documentMargin() * 2

        self.setFixedWidth(int(a))
        self.setFixedHeight(ceil(self.document().size().height()))
        
    # def __adjust_height(self) -> None:
        
    #     viewport_width = self.viewport().width()
    #     self.document().setTextWidth(viewport_width)

    #     a = self.document().idealWidth() + self.document().documentMargin() * 2

    #     self.setFixedWidth(int(a))
    #     self.setFixedHeight(ceil(self.document().size().height()))