from .widgets.login.LoginWidget import LoginWidget
from .MainWindowQSS import MainWindowQSS
from .widgets.chat.ChatWidget import ChatWidget
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtGui
from os.path import (
    dirname, realpath,
)

#self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
class MainWindow(QMainWindow):

    def __init__(self) -> None:
        
        super().__init__()

        self.__screen_size = QApplication.primaryScreen().size()

        self.__set_window_geometry()
        
        self.__add_app_font()

        central_widget = ChatWidget(self)
        # central_widget = LoginWidget(self)

        self.setCentralWidget(central_widget)
        
        self.setStyleSheet(MainWindowQSS().qss)

    @staticmethod
    def __add_app_font() -> None:

        font_path = f"{dirname(realpath(__file__))}\\appFont.ttf"
        
        QtGui.QFontDatabase.addApplicationFont(font_path)
        
    def __set_window_geometry(self) -> None:

        self.setFixedWidth(int(self.__screen_size.width() / 1.5))
        self.setFixedHeight(int(self.__screen_size.height() / 1.5))
