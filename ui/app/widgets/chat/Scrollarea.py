from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QFrame

class Scrollarea(QScrollArea):

    def __init__(self, showed_object_name: str, hidden_object_name: str) -> None:

        if not isinstance(showed_object_name, str):
            raise TypeError(type(showed_object_name))
        
        if not isinstance(hidden_object_name, str):
            raise TypeError(type(hidden_object_name))

        super().__init__()

        self.__showed_object_name = showed_object_name
        self.__hidden_object_name = hidden_object_name

        self.__layout = self.__get_layout()

        self.verticalScrollBar().setObjectName(self.__hidden_object_name)

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
            scrollbar.setObjectName(self.__showed_object_name)
            scrollbar.setStyleSheet("")

    def leaveEvent(self, event: QtCore.QEvent | None) -> None:
        
        super().leaveEvent(event)

        scrollbar = self.verticalScrollBar()

        if scrollbar.objectName() != self.__hidden_object_name:
            scrollbar.setObjectName(self.__hidden_object_name)
            scrollbar.setStyleSheet("")
