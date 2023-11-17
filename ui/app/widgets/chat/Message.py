from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QTextOption, QResizeEvent
from PyQt6 import QtCore

class Message(QTextEdit):
    
    def __init__(self, id: int, text: str):

        if not isinstance(id, int):
            raise TypeError(type(id))
        
        if not isinstance(text, str):
            raise TypeError(type(text))

        super().__init__()

        self.__id = id

        self.setWordWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)        
        self.textChanged.connect(self.__adjust_size)
        self.setText(text)
        self.setReadOnly(True)
        self.verticalScrollBar().setDisabled(True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    @property
    def id(self) -> int:
        return self.__id

    def resizeEvent(self, _: QResizeEvent) -> None:

        self.__adjust_size()
        
    def __adjust_size(self) -> None:
        
        viewport_width = self.viewport().width()
        margin = self.document().documentMargin()
        paddings = self.contentsMargins()

        self.document().setTextWidth(viewport_width)

        width = int(self.document().idealWidth() + paddings.left() + paddings.right())
        height = int(self.document().size().height() + margin + paddings.top() + paddings.bottom())

        self.setFixedWidth(width)
        self.setFixedHeight(height)
