from PyQt6.QtWidgets import QTextEdit, QWidget
from PyQt6 import QtCore

class MessageEdit(QTextEdit):

    def __init__(self, parent: QWidget, max_height: int):

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        if not isinstance(max_height, int):
            raise TypeError(type(max_height))

        super().__init__(parent)

        self.__max_height = max_height

        self.textChanged.connect(self.__adjust_height)
        self.installEventFilter(self)

    def eventFilter(self, object: QtCore.QObject | None, event: QtCore.QEvent | None) -> bool:

        if event.type() == QtCore.QEvent.Type.KeyPress and object is self and event.key() == QtCore.Qt.Key.Key_Return and self.hasFocus():
            print('Enter pressed')
            
        return False
    
    def resizeEvent(self, event: QtCore.QEvent | None) -> None:

        super().resizeEvent(event)

        self.__adjust_height()

    def __adjust_height(self):

        document_height = int(self.document().size().height())

        if document_height <= self.__max_height:
            self.setFixedHeight(document_height)
