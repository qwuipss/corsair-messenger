from .LoginWidgetQSS import LoginWidgetQSS

from PyQt6.QtCore import (
    Qt, QSize, 
)

from PyQt6.QtWidgets import (
    QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem,
)

class LoginWidget(QWidget):

    def __init__(self, screen_size: QSize) -> None:

        super().__init__()

        self.__layout = QVBoxLayout()

        self.__login_widget_qss = LoginWidgetQSS(screen_size)

        label_layout = self.__get_logo_label_layout()
        login_layout = self.__get_login_layout()
        password_layout = self.__get_password_layout()
        enter_layout = self.__get_enter_layout()

        self.__layout.addLayout(label_layout)
        #self.__layout.addSpacerItem(QSpacerItem(0, -60))
        self.__layout.addLayout(login_layout)
        self.__layout.addLayout(password_layout)
        self.__layout.addLayout(enter_layout)


    @property
    def layout(self) -> QVBoxLayout:
        return  self.__layout

    def __get_logo_label_layout(self) -> QVBoxLayout:
        
        logo_label_layout = QVBoxLayout()

        logo_label = QLabel(self.__login_widget_qss.logo_label_text)

        logo_label_layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        logo_label.setStyleSheet(self.__login_widget_qss.logo_label_qss)

        return logo_label_layout

    def __get_login_layout(self) -> QVBoxLayout:
        
        login_layout = QVBoxLayout()

        login_label = QLabel(self.__login_widget_qss.login_label_text)

        login_layout.addWidget(login_label, alignment=Qt.AlignmentFlag.AlignCenter)

        login_layout.addWidget(QLineEdit(), alignment=Qt.AlignmentFlag.AlignCenter)

        login_label.setStyleSheet(self.__login_widget_qss.login_label_qss)

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
    