from .widgets.login.LoginWidget import LoginWidget
from client.Client import Client
from SharedConstants import SECOND_WINDOW
from .MainWindowQSS import MainWindowQSS
from .widgets.chat.ChatWidget import ChatWidget
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtGui
from os.path import dirname, realpath

#self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
class MainWindow(QMainWindow):

    if SECOND_WINDOW:
        __second_window_geometry_set = False

    def __init__(self) -> None:
        
        super().__init__()

        self.__screen_size = QApplication.primaryScreen().size()

        self.__set_window_size()
        self.__set_window_geometry()
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

    def __set_window_geometry(self) -> None:
        
        rect = self.rect()
            
        if SECOND_WINDOW and not MainWindow.__second_window_geometry_set:
            
            self.setGeometry(-int(rect.width() * 1.1), int(rect.height() * .2), rect.width(), rect.height())

            MainWindow.__second_window_geometry_set = True

        else:

            self.setGeometry(int(rect.width() * .2), int(rect.height() * .2), rect.width(), rect.height())

    def __switch_login_to_chat(self) -> None:

        self.setCentralWidget(ChatWidget(self, self.__client))