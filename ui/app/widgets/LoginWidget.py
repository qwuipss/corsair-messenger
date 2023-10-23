from ..qss import LOGIN_WIDGET_QSS
from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
                             QVBoxLayout, 
                             QLabel, 
                             QLineEdit, 
                             QPushButton,
                             QSpacerItem,
                             QWidget,
                            )

class LoginWidget(QWidget):

    def __init__(self, screen_size: QSize) -> None:
        
        if not isinstance(screen_size, QSize):
            raise TypeError(type(screen_size))

        super().__init__()

        self.__layout = QVBoxLayout()

        label_layout = self.__get_label_layout()
        login_layout = self.__get_login_layout()
        password_layout = self.__get_password_layout()
        enter_layout = self.__get_enter_layout()

        self.__layout.addLayout(label_layout)
        self.__layout.addSpacerItem(QSpacerItem(0, 30))
        self.__layout.addLayout(login_layout)
        self.__layout.addSpacerItem(QSpacerItem(0, 30))
        self.__layout.addLayout(password_layout)
        self.__layout.addSpacerItem(QSpacerItem(0, 30))
        self.__layout.addLayout(enter_layout)
        self.__layout.addSpacerItem(QSpacerItem(0, 30))

        self.setStyleSheet(LOGIN_WIDGET_QSS)
    
    @property
    def layout(self):
        return self.__layout

    def __get_label_layout(self) -> QVBoxLayout:
        
        label_layout = QVBoxLayout()

        label = QLabel("CORSAIR")
        label.setObjectName("label")

        label_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        label.setStyleSheet(LOGIN_WIDGET_QSS)

        return label_layout

    def __get_login_layout(self) -> QVBoxLayout:
        
        login_layout = QVBoxLayout()

        login_layout.addWidget(QLabel("Login"), alignment=Qt.AlignmentFlag.AlignCenter)
        login_layout.addWidget(QLineEdit(), alignment=Qt.AlignmentFlag.AlignCenter)

        return login_layout

    def __get_password_layout(self) -> QVBoxLayout:

        password_layout = QVBoxLayout()

        password_label = QLabel("Password")
        password_layout.addWidget(password_label, alignment=Qt.AlignmentFlag.AlignCenter)

        password_line_edit = QLineEdit()
        password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        password_layout.addWidget(password_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        return password_layout

    def __get_enter_layout(self) -> QVBoxLayout:

        enter_layout = QVBoxLayout()

        enter_button = QPushButton("Enter")
        enter_layout.addWidget(enter_button, alignment=Qt.AlignmentFlag.AlignCenter)

        return enter_layout
    