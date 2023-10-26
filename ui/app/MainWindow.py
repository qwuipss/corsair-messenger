from .widgets.login.LoginWidget import LoginWidget
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
        
        self.__central_widget = QWidget(self)

        self.__central_widget.setLayout(LoginWidget(self.size(), MainWindow.__get_font_id()).layout)

        self.setCentralWidget(self.__central_widget)

        self.setStyleSheet(QSSHelper.concat(
            QSSHelper.background_color(MainWindowSharedQSS.BACKGROUND_COLOR),
            QSSHelper.color(MainWindowSharedQSS.COLOR),
        ))

    @staticmethod
    def __get_font_id():

        font_path = rf"{dirname(realpath(__file__))}\appFont.ttf"
        font_id = QtGui.QFontDatabase.addApplicationFont(font_path)

        return font_id

    def __set_window_geometry(self):

        self.setFixedWidth(int(self.__screen_size.width() / 1.5))
        self.setFixedHeight(int(self.__screen_size.height() / 1.5))
