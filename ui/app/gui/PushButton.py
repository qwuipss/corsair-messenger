from PyQt6.QtWidgets import QPushButton, QWidget
from PyQt6.QtGui import QIcon, QPixmap, QEnterEvent

class PushButton(QPushButton):

    def __init__(self, parent: QWidget, default_icon_path: str, hover_icon_path: str) -> None:

        super().__init__(parent)
        
        self.__hover_icon = QIcon(QPixmap(hover_icon_path))

        self.__default_icon = QIcon(QPixmap(default_icon_path))
        self.setIcon(self.__default_icon)
        
    def enterEvent(self, _: QEnterEvent):  
        self.setIcon(self.__hover_icon)

    def leaveEvent(self, _: QEnterEvent):
        self.setIcon(self.__default_icon)
