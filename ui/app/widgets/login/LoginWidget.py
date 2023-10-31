from managers.RegexManager import RegexManager
from .LoginWidgetQSS import LoginWidgetQSS
from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem,
)

class LoginWidget(QWidget):

    def __init__(self, parent: QWidget, font_id: int) -> None:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        if not isinstance(font_id, int):
            raise TypeError(type(font_id))

        super().__init__()

        self.__font = QtGui.QFont(QtGui.QFontDatabase.applicationFontFamilies(font_id)[0])

        layout = QVBoxLayout()

        parent_size = parent.size()

        self.__login_widget_qss = LoginWidgetQSS(parent_size)

        screen_height = parent_size.height()

        line_edit_width = int(parent_size.width() / 3.4)
        vertical_spacer = -screen_height // 7

        label_layout = self.__get_logo_label_layout()
        login_layout = self.__get_login_layout(line_edit_width, vertical_spacer)
        password_layout = self.__get_password_layout(line_edit_width, vertical_spacer)
        enter_layout = self.__get_enter_layout()

        layout = self.__get_main_layout(label_layout, login_layout, password_layout, enter_layout, screen_height)

        self.setLayout(layout)

    def __get_main_layout(
        self, 
        label_layout: QVBoxLayout, login_layout: QVBoxLayout, password_layout: QVBoxLayout, enter_layout: QVBoxLayout, 
        screen_height: int) -> QVBoxLayout:
        
        if not isinstance(label_layout, QVBoxLayout):
            raise TypeError(type(label_layout))
        
        if not isinstance(login_layout, QVBoxLayout):
            raise TypeError(type(login_layout))
        
        if not isinstance(password_layout, QVBoxLayout):
            raise TypeError(type(password_layout))
        
        if not isinstance(enter_layout, QVBoxLayout):
            raise TypeError(type(enter_layout))
        
        if not isinstance(screen_height, int):
            raise TypeError(type(screen_height))
        
        vertical_spacer = -screen_height // 15
        
        layout = QVBoxLayout()

        layout.addLayout(label_layout)
        layout.addLayout(login_layout)
        layout.addLayout(password_layout)
        layout.addSpacerItem(QSpacerItem(0, vertical_spacer))
        layout.addLayout(enter_layout)

        return layout

    def __get_logo_label_layout(self) -> QVBoxLayout:
        
        logo_label_layout = QVBoxLayout()

        logo_label = self.__get_logo_label()

        logo_label_layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignCenter)

        return logo_label_layout

    def __get_login_layout(self, line_edit_width: int, vertical_spacer: int) -> QVBoxLayout:
        
        if not isinstance(line_edit_width, int):
            raise TypeError(type(line_edit_width))
        
        if not isinstance(vertical_spacer, int):
            raise TypeError(type(vertical_spacer))

        login_layout = QVBoxLayout()

        login_label = self.__get_login_label()
        login_line_edit = self.__get_login_line_edit(line_edit_width)

        login_layout.addWidget(login_label, alignment=Qt.AlignmentFlag.AlignCenter)
        login_layout.addSpacerItem(QSpacerItem(0, vertical_spacer))
        login_layout.addWidget(login_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        return login_layout

    def __get_password_layout(self, line_edit_width: int, vertical_spacer: int) -> QVBoxLayout:

        if not isinstance(line_edit_width, int):
            raise TypeError(type(line_edit_width))
        
        if not isinstance(vertical_spacer, int):
            raise TypeError(type(vertical_spacer))

        password_layout = QVBoxLayout()

        password_label = self.__get_password_label()
        password_line_edit = self.__get_password_line_edit(line_edit_width)
        
        password_layout.addWidget(password_label, alignment=Qt.AlignmentFlag.AlignCenter)
        password_layout.addSpacerItem(QSpacerItem(0, vertical_spacer))
        password_layout.addWidget(password_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        return password_layout

    def __get_enter_layout(self) -> QVBoxLayout:

        enter_layout = QVBoxLayout()

        enter_button = self.__get_enter_button()

        enter_layout.addWidget(enter_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        return enter_layout
    
    def __get_logo_label(self) -> QLabel:

        logo_label = QLabel(LoginWidgetQSS.LOGO_LABEL_TEXT)

        logo_label.setFont(self.__font)
        logo_label.setStyleSheet(self.__login_widget_qss.logo_label_qss)

        return logo_label

    def __get_login_label(self) -> QLabel:

        login_label = QLabel(LoginWidgetQSS.LOGIN_LABEL_TEXT)

        login_label.setFont(self.__font)
        login_label.setStyleSheet(self.__login_widget_qss.line_edit_label_qss)

        return login_label

    def __get_login_line_edit(self, width: int) -> QLineEdit:
        
        if not isinstance(width, int):
            raise TypeError(type(width))

        login_line_edit = QLineEdit()
        
        line_edit_validator = RegexManager.get_regex_nickname_validator()

        login_line_edit.setMaxLength(25)
        login_line_edit.setValidator(line_edit_validator)
        login_line_edit.setFixedWidth(width)
        login_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        login_line_edit.setStyleSheet(self.__login_widget_qss.line_edit_qss)
        login_line_edit.setFont(self.__font)

        return login_line_edit

    def __get_password_label(self) -> QLabel:
        
        password_label = QLabel(LoginWidgetQSS.PASSWORD_LABEL_TEXT)        
        password_label.setFont(self.__font)
        password_label.setStyleSheet(self.__login_widget_qss.line_edit_label_qss)

        return password_label

    def __get_password_line_edit(self, width: int) -> QLineEdit:

        if not isinstance(width, int):
            raise TypeError(type(width))

        password_line_edit = QLineEdit()

        password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        password_line_edit.setMaxLength(30)
        password_line_edit.setFixedWidth(width)
        password_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        password_line_edit.setStyleSheet(self.__login_widget_qss.line_edit_qss)

        return password_line_edit
    
    def __get_enter_button(self) -> QPushButton:

        enter_button = QPushButton(LoginWidgetQSS.ENTER_BUTTON_LABEL_TEXT)

        enter_button.setFont(self.__font)
        enter_button.setCursor(Qt.CursorShape.PointingHandCursor)
        enter_button.setStyleSheet(self.__login_widget_qss.enter_button_qss)

        return enter_button