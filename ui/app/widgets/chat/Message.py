from PyQt6.QtGui import QPainter, QTextOption, QPaintEvent, QFontMetrics, QFont
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

class Message(QLabel):
    
    def __init__(self, text: str, parent: QWidget):

        if not isinstance(text, str):
            raise TypeError(type(text))

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        # a = QFontMetrics(QFont("Kanita", 13))
        # d = a.horizontalAdvance(text) // 550 - 1

        super().__init__(text, parent)

        
        # self.setText(text + "\n" * d)

        self.setWordWrap(True)
        self.setObjectName("message")
        # self.setContentsMargins(0,0,0,0)
        # self.
        self.setMinimumHeight(self.height())

    def paintEvent(self, _: QPaintEvent | None):
        
        painter = QPainter(self)
        
        option = QTextOption()

        option.setWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
        
        painter.drawText(self.rect().toRectF(), self.text(), option)
