from .widgets.login.LoginWidget import LoginWidget
from .widgets.chat.ChatWidget import ChatWidget
from .SharedQSS import MainWindowSharedQSS
from helpers.QSSHelper import QSSHelper
from PyQt6 import QtGui
from os.path import (
    dirname, realpath,
)
from PyQt6.QtWidgets import (
    QWidget, QMainWindow, QApplication,
)

#self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        
        super().__init__()

        self.__screen_size = QApplication.primaryScreen().size()

        self.__set_window_geometry()
        
        self.__font_id = self.__add_app_font()

        central_widget = ChatWidget(self, self.__font_id)
        
        central_widget.setContentsMargins(0, 0, 0, 0)

        self.setCentralWidget(central_widget)

        self.setStyleSheet(QSSHelper.concat(
            QSSHelper.background_color(MainWindowSharedQSS.BACKGROUND_COLOR),
            QSSHelper.color(MainWindowSharedQSS.COLOR),
        ))

    @staticmethod
    def __add_app_font() -> int:

        font_path = rf"{dirname(realpath(__file__))}\appFont.ttf"
        font_id = QtGui.QFontDatabase.addApplicationFont(font_path)

        return font_id

    def __set_window_geometry(self) -> None:

        self.setFixedWidth(int(self.__screen_size.width() / 1.5))
        self.setFixedHeight(int(self.__screen_size.height() / 1.5))
