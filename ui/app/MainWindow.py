from .widgets.login.LoginWidget import LoginWidget
from client.Client import Client
from .MainWindowQSS import MainWindowQSS
from .widgets.chat.ChatWidget import ChatWidget
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtGui
from os.path import dirname, realpath
from threading import Thread
import asyncio

#self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
class MainWindow(QMainWindow):

    def __init__(self) -> None:
        
        super().__init__()

        self.__screen_size = QApplication.primaryScreen().size()

        self.__set_window_size()
        self.__add_app_font()

        client = Client()

        client_thread = Thread(target=lambda: asyncio.run(client.start_receiving()))
        client_thread.setDaemon(True)
        client_thread.start()
        
        central_widget = ChatWidget(self, client)
        # central_widget = LoginWidget(self)

        self.setCentralWidget(central_widget)
        
        self.setStyleSheet(MainWindowQSS().qss)

    @staticmethod
    def __add_app_font() -> None:

        font_path = f"{dirname(realpath(__file__))}/appFont.ttf"
        
        QtGui.QFontDatabase.addApplicationFont(font_path)
        
    def __set_window_size(self) -> None:

        self.setFixedWidth(int(self.__screen_size.width() * .7))
        self.setFixedHeight(int(self.__screen_size.height() * .7))
