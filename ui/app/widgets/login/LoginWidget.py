from managers.RegexManager import RegexManager
from .LoginWidgetQSS import LoginWidgetQSS
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem, QMainWindow

class LoginWidget(QWidget):

    def __init__(self, main_window: QMainWindow) -> None:

        if not isinstance(main_window, QMainWindow):
            raise TypeError(type(main_window))

        super().__init__(main_window)

        layout = QVBoxLayout()

        self.__login_widget_qss = LoginWidgetQSS(main_window)

        window_height = main_window.size().height()

        vertical_spacer = int(-window_height * .143)

        logo_label_layout = self.__get_logo_label_layout()
        login_layout = self.__get_login_layout(vertical_spacer)
        password_layout = self.__get_password_layout(vertical_spacer)
        enter_layout = self.__get_enter_layout()

        layout = self.__get_main_layout(logo_label_layout, login_layout, password_layout, enter_layout, window_height)

        self.setLayout(layout)
        self.setStyleSheet(self.__login_widget_qss.qss)

    def __get_main_layout(
        self, 
        label_layout: QVBoxLayout, login_layout: QVBoxLayout, password_layout: QVBoxLayout, enter_layout: QVBoxLayout, 
        window_height: int) -> QVBoxLayout:
        
        if not isinstance(label_layout, QVBoxLayout):
            raise TypeError(type(label_layout))
        
        if not isinstance(login_layout, QVBoxLayout):
            raise TypeError(type(login_layout))
        
        if not isinstance(password_layout, QVBoxLayout):
            raise TypeError(type(password_layout))
        
        if not isinstance(enter_layout, QVBoxLayout):
            raise TypeError(type(enter_layout))
        
        if not isinstance(window_height, int):
            raise TypeError(type(window_height))
        
        vertical_spacer = int(-window_height * .0667)
        
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

    def __get_login_layout(self, vertical_spacer: int) -> QVBoxLayout:
        
        if not isinstance(vertical_spacer, int):
            raise TypeError(type(vertical_spacer))

        login_layout = QVBoxLayout()

        login_label = self.__get_login_label()
        login_line_edit = self.__get_login_line_edit()

        login_layout.addWidget(login_label, alignment=Qt.AlignmentFlag.AlignCenter)
        login_layout.addSpacerItem(QSpacerItem(0, vertical_spacer))
        login_layout.addWidget(login_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        return login_layout

    def __get_password_layout(self, vertical_spacer: int) -> QVBoxLayout:

        if not isinstance(vertical_spacer, int):
            raise TypeError(type(vertical_spacer))

        password_layout = QVBoxLayout()

        password_label = self.__get_password_label()
        password_line_edit = self.__get_password_line_edit()
        
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

        logo_label = QLabel("CORSAIR", self)

        logo_label.setObjectName("logoLabel")

        return logo_label

    def __get_login_label(self) -> QLabel:

        login_label = QLabel("Login", self)

        login_label.setObjectName("loginLabel")

        return login_label

    def __get_login_line_edit(self) -> QLineEdit:
        
        login_line_edit = QLineEdit(self)

        line_edit_validator = RegexManager.get_regex_nickname_validator()

        login_line_edit.setObjectName("loginEdit")
        login_line_edit.setMaxLength(25)
        login_line_edit.setValidator(line_edit_validator)
        login_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        return login_line_edit

    def __get_password_label(self) -> QLabel:
        
        password_label = QLabel("Password", self)       

        password_label.setObjectName("passwordLabel")

        return password_label

    def __get_password_line_edit(self) -> QLineEdit:

        password_line_edit = QLineEdit(self)

        password_line_edit.setObjectName("passwordEdit")
        password_line_edit.setMaxLength(30)
        password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        password_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        return password_line_edit
    
    def __get_enter_button(self) -> QPushButton:

        enter_button = QPushButton("Enter", self)

        enter_button.setObjectName("enterButton")
        enter_button.setCursor(Qt.CursorShape.PointingHandCursor)

        return enter_button