from .qss import *
from .widgets.LoginWidget import LoginWidget
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
                             QWidget, 
                             QMainWindow,
                             QApplication,
                            )

#self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        
        super().__init__()

        #self.setWindowTitle(WINDOW_TITLE)

        primary_screen = QApplication.primaryScreen()
        geometry = primary_screen.geometry()
        aspectRatio = primary_screen.devicePixelRatio()
        
        self.__primary_screen_size = QSize(int(geometry.width() * aspectRatio), int(geometry.height() * aspectRatio))

        self.__central_widget = QWidget(self)

        login_widget = LoginWidget(self.__primary_screen_size)

        self.__central_widget.setLayout(login_widget.layout)

        self.setCentralWidget(self.__central_widget)
