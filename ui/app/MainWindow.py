from .widgets.login.LoginWidget import LoginWidget
from client.Client import Client
from .MainWindowQSS import MainWindowQSS
from .widgets.chat.ChatWidget import ChatWidget
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtGui
from os.path import dirname, realpath

#self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
class MainWindow(QMainWindow):

    def __init__(self) -> None:
        
        super().__init__()

        self.__screen_size = QApplication.primaryScreen().size()

        self.__set_window_size()
        self.__add_app_font()

        self.__client = Client()

        if self.__client.is_authorized:
            central_widget = ChatWidget(self, self.__client)
        else:
            central_widget = LoginWidget(self, self.__client, self.__switch_login_to_chat)

        self.setCentralWidget(central_widget)        
        self.setStyleSheet(MainWindowQSS().qss)

    @staticmethod
    def __add_app_font() -> None:

        font_path = f"{dirname(realpath(__file__))}/appFont.ttf"
        
        QtGui.QFontDatabase.addApplicationFont(font_path)
        
    def __set_window_size(self) -> None:

        self.setFixedWidth(int(self.__screen_size.width() * .7))
        self.setFixedHeight(int(self.__screen_size.height() * .7))

    def __switch_login_to_chat(self) -> None:

        self.setCentralWidget(ChatWidget(self, self.__client))