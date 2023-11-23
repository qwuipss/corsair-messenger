from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QTextOption, QResizeEvent, QTextCursor
from PyQt6 import QtCore

class Message(QTextEdit):
    
    def __init__(self, id: int, text: str):

        if not isinstance(id, int):
            raise TypeError(type(id))

        if not isinstance(text, str):
            raise TypeError(type(text))

        super().__init__()

        self.__id = id
        self.__text = text

        self.setWordWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)        
        self.textChanged.connect(self.__adjust_size)
        self.setText(self.__text)
        self.setReadOnly(True)
        self.verticalScrollBar().setDisabled(True)
        self.horizontalScrollBar().setDisabled(True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.verticalScrollBar().valueChanged.connect(self.__prevent_scroll_on_selection_if_needed)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def text(self) -> str:
        return self.__text

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

    def __prevent_scroll_on_selection_if_needed(self):

        if self.verticalScrollBar().value() != 0:
            self.textCursor().movePosition(QTextCursor.MoveOperation.End)
            self.verticalScrollBar().setValue(0)
            