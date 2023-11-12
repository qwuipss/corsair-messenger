from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QFrame

class Scrollarea(QScrollArea):

    def __init__(self, parent: QWidget) -> None:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        super().__init__(parent)

        self.__layout = self.__get_layout(parent)

        self.verticalScrollBar().hide()

    @property
    def layout(self) -> QVBoxLayout:
        return self.__layout
    
    def __get_layout(self, parent: QWidget) -> QVBoxLayout:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        layout = QVBoxLayout(self)

        widget = QWidget(parent)

        widget.setLayout(layout)

        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFrameShape(QFrame.Shape(0))
        self.setWidget(widget)

        return layout
    
    def enterEvent(self, event: QtGui.QEnterEvent | None) -> None:

        super().enterEvent(event)

        scrollbar = self.verticalScrollBar()

        if scrollbar.maximum() != 0:
            scrollbar.show()

    def leaveEvent(self, event: QtCore.QEvent | None) -> None:
        
        super().leaveEvent(event)

        scrollbar = self.verticalScrollBar()

        if not scrollbar.isHidden():
            scrollbar.hide()
