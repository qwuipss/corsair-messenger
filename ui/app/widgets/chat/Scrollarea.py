from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QFrame

class Scrollarea(QScrollArea):

    def __init__(self) -> None:

        super().__init__()

        self.__layout = self.__get_layout()

        self.verticalScrollBar().hide()

    @property
    def layout(self) -> QVBoxLayout:
        return self.__layout
    
    def __get_layout(self) -> QVBoxLayout:

        layout = QVBoxLayout(self)

        widget = QWidget()

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
