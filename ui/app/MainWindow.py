from .widgets.login.LoginWidget import LoginWidget
from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QWidget, QMainWindow, QApplication,
)

#self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        
        super().__init__()

        self.__screen_size = QApplication.primaryScreen().size()

        self.__central_widget = QWidget(self)

        self.__central_widget.setLayout(LoginWidget(self.__screen_size).layout)

        self.setCentralWidget(self.__central_widget)

        self.__set_window_geometry()

        # todo 
        self.setStyleSheet(QSSHelper.concat(
            QSSHelper.background_color("f2f2f2"),
            QSSHelper.color((240, 240, 240)),
        ))

    def __set_window_geometry(self):

        self.setFixedWidth(int(self.__screen_size.width() / 1.5))
        self.setFixedHeight(int(self.__screen_size.height() / 1.5))
