from PyQt6.QtWidgets import QTextEdit, QWidget
from PyQt6 import QtCore
from ...SharedQSS import SharedQSS
from PyQt6 import QtGui

class MessageEdit(QTextEdit):

    def __init__(self, parent: QWidget, max_height: int):

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        if not isinstance(max_height, int):
            raise TypeError(type(max_height))

        super().__init__(parent)

        self.__max_height = max_height

        placeholder_palette = self.palette()
        placeholder_palette.setColor(QtGui.QPalette.ColorRole.PlaceholderText, QtGui.QColor(f"#{SharedQSS.COLOR_555555}"))  

        self.textChanged.connect(self.__adjust_height)
        self.setPalette(placeholder_palette)
        self.setPlaceholderText("Write a message...")
        self.installEventFilter(self)

    def eventFilter(self, object: QtCore.QObject | None, event: QtCore.QEvent | None) -> bool:

        super().eventFilter(object, event)

        if event.type() == QtCore.QEvent.Type.KeyPress and object is self and event.key() == QtCore.Qt.Key.Key_Return and self.hasFocus():
            print('Enter pressed')
            
        return False
    
    def resizeEvent(self, event: QtCore.QEvent | None) -> None:

        super().resizeEvent(event)

        self.__adjust_height()

    def __adjust_height(self) -> None:

        document_height = int(self.document().size().height())
        paddings = self.contentsMargins()

        if document_height <= self.__max_height:
            self.setFixedHeight(document_height + paddings.top() + paddings.bottom())
