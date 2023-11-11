from PyQt6.QtWidgets import QWidget, QTextEdit
from PyQt6.QtGui import QTextOption, QResizeEvent

class Message(QTextEdit):
    
    def __init__(self, text: str, parent: QWidget):

        if not isinstance(text, str):
            raise TypeError(type(text))
        
        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        super().__init__(parent)

        self.setWordWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
        
        self.textChanged.connect(self.__adjust_size)

        self.setText(text)
        self.setReadOnly(True)

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

        