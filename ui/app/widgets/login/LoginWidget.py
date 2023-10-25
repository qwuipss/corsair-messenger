from .LoginWidgetQSS import LoginWidgetQSS

from PyQt6.QtCore import (
    Qt, QSize, 
)

from PyQt6.QtWidgets import (
    QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem,
)

class LoginWidget(QWidget):

    def __init__(self, screen_size: QSize) -> None:

        if not isinstance(screen_size, QSize):
            raise TypeError(type(screen_size))

        super().__init__()

        self.__layout = QVBoxLayout()

        self.__login_widget_qss = LoginWidgetQSS(screen_size)

        screen_height = screen_size.height()

        line_edit_width = int(screen_size.width() / 6)
        vertical_spacer = int(-screen_height / 11)

        label_layout = self.__get_logo_label_layout()
        login_layout = self.__get_login_layout(line_edit_width, vertical_spacer)
        password_layout = self.__get_password_layout(line_edit_width, vertical_spacer)
        enter_layout = self.__get_enter_layout()

        self.__layout.addLayout(label_layout)
        self.__layout.addLayout(login_layout)
        self.__layout.addLayout(password_layout)

        vertical_spacer = int(-screen_height / 25)
        
        self.__layout.addSpacerItem(QSpacerItem(0, vertical_spacer))

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

    def __get_login_layout(self, line_edit_width: int, vertical_spacer: int) -> QVBoxLayout:
        
        if not isinstance(line_edit_width, int):
            raise TypeError(type(line_edit_width))
        
        if not isinstance(vertical_spacer, int):
            raise TypeError(type(vertical_spacer))

        login_layout = QVBoxLayout()

        login_label = QLabel(self.__login_widget_qss.login_label_text)

        login_line_edit = QLineEdit()

        login_layout.addWidget(login_label, alignment=Qt.AlignmentFlag.AlignCenter)
        login_layout.addSpacerItem(QSpacerItem(0, vertical_spacer))
        login_layout.addWidget(login_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        login_line_edit.setFixedWidth(line_edit_width)

        login_label.setStyleSheet(self.__login_widget_qss.line_edit_label_qss)
        login_line_edit.setStyleSheet(self.__login_widget_qss.line_edit_qss)

        return login_layout

    def __get_password_layout(self, line_edit_width: int, vertical_spacer: int) -> QVBoxLayout:

        if not isinstance(line_edit_width, int):
            raise TypeError(type(line_edit_width))
        
        if not isinstance(vertical_spacer, int):
            raise TypeError(type(vertical_spacer))

        password_layout = QVBoxLayout()

        password_label = QLabel(self.__login_widget_qss.password_label_text)

        password_line_edit = QLineEdit()
        password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        password_layout.addWidget(password_label, alignment=Qt.AlignmentFlag.AlignCenter)
        password_layout.addSpacerItem(QSpacerItem(0, vertical_spacer))
        password_layout.addWidget(password_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        password_line_edit.setFixedWidth(line_edit_width)

        password_label.setStyleSheet(self.__login_widget_qss.line_edit_label_qss)
        password_line_edit.setStyleSheet(self.__login_widget_qss.line_edit_qss)

        return password_layout

    def __get_enter_layout(self) -> QVBoxLayout:

        enter_layout = QVBoxLayout()

        enter_button = QPushButton(self.__login_widget_qss.enter_button_text)
        enter_button.setCursor(Qt.CursorShape.PointingHandCursor)

        enter_layout.addWidget(enter_button, alignment=Qt.AlignmentFlag.AlignCenter)

        enter_button.setStyleSheet(self.__login_widget_qss.enter_button_qss)

        return enter_layout
    