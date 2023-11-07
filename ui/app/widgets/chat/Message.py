from PyQt6 import QtCore
from .MessageEdit import MessageEdit
from PyQt6.QtWidgets import QWidget, QTextEdit, QLabel, QSizePolicy, QPlainTextEdit
from PyQt6.QtGui import QPaintEvent, QPainter, QTextOption, QFontMetrics, QFont, QTextLayout, QTextDocument
from PyQt6.QtCore import QRect

class Message(QTextEdit):
    
    def __init__(self, text: str, parent: QWidget):

        if not isinstance(text, str):
            raise TypeError(type(text))
        
        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        super().__init__(parent)

        self.setWordWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
        self.setFixedWidth(550)
        self.setObjectName("message")
        
        self.textChanged.connect(self.autoResize)

        self.setText(text)

    def autoResize(self):
        self.document().setTextWidth(self.viewport().width())
        margins = self.contentsMargins()
        height = int(self.document().size().height() + margins.top() + margins.bottom())
        self.setFixedHeight(height)

    def resizeEvent(self, event):
        self.autoResize()
    # def paintEvent(self, _: QPaintEvent | None):
        
    #     painter = QPainter(self)
        
    #     option = QTextOption()

    #     option.setWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)

    #     painter.drawText(self.rect().toRectF(), self._text, option)

    # def resizeEvent(self, event: QtCore.QEvent | None) -> None:

    #     super().resizeEvent(event)

    #     self.__adjust_height()

    # def __adjust_height(self) -> None:

    #     document_height = int(self.document().size().height())

    #     self.setFixedHeight(document_height)
