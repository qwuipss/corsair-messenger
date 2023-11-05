from collections.abc import Callable
from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QFrame, QMainWindow

class Scrollarea(QScrollArea):

    def __init__(self, parent: QWidget, enter_event: Callable[[], None], leave_event: Callable[[], None]) -> None:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        if not isinstance(enter_event, Callable):
            raise TypeError(type(enter_event))
        
        if not isinstance(leave_event, Callable):
            raise TypeError(type(leave_event))
        
        super().__init__(parent)

        self.__enter_event = enter_event
        self.__leave_event = leave_event

        self.__layout = self.__get_layout(parent) 
        
    @property
    def layout(self) -> QVBoxLayout:
        return self.__layout
    
    def add_widget(self, widget: QWidget) -> None:

        if not isinstance(widget, QWidget):
            raise TypeError(type(widget))        

        self.__layout.addWidget(widget)

    def __get_layout(self, parent: QWidget) -> QVBoxLayout:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        layout = QVBoxLayout()

        widget = QWidget(parent)

        widget.setLayout(layout)

        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFrameShape(QFrame.Shape(0))
        self.setWidget(widget)

        return layout
    
    def enterEvent(self, event: QtGui.QEnterEvent | None) -> None:

        super().enterEvent(event)

        self.__enter_event()

    def leaveEvent(self, event: QtCore.QEvent | None) -> None:
        
        super().leaveEvent(event)

        self.__leave_event()
    