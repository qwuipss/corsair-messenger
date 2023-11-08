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
        self.setObjectName("message")
        
        self.textChanged.connect(self.__adjust_height)

        self.setText(text)
        self.setReadOnly(True)

    def resizeEvent(self, _: QResizeEvent) -> None:

        self.__adjust_height()
        
    def __adjust_height(self) -> None:
        
        width = self.width()
        a = self.viewport().width()
        self.document().setTextWidth(a)
        # self.document().text

        self.setFixedHeight(int(self.document().size().height()))        
        # self.setFixedWidth(width)