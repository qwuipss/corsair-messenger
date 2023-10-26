from .LoginWidgetQSS import LoginWidgetQSS
from PyQt6 import QtGui
from PyQt6 import QtCore
from PyQt6.QtCore import (
    Qt, QSize, 
)
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
        vertical_spacer = int(-screen_height / 7)

        label_layout = self.__get_logo_label_layout()
        login_layout = self.__get_login_layout(line_edit_width, vertical_spacer)
        password_layout = self.__get_password_layout(line_edit_width, vertical_spacer)
        enter_layout = self.__get_enter_layout()

        layout.addLayout(label_layout)
        layout.addLayout(login_layout)
        layout.addLayout(password_layout)

        vertical_spacer = int(-screen_height / 15)
        
        layout.addSpacerItem(QSpacerItem(0, vertical_spacer))

        layout.addLayout(enter_layout)

        self.setLayout(layout)

    def __get_logo_label_layout(self) -> QVBoxLayout:
        
        logo_label_layout = QVBoxLayout()

        logo_label = QLabel(self.__login_widget_qss.logo_label_text)

        logo_label_layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignCenter)

        logo_label.setStyleSheet(self.__login_widget_qss.logo_label_qss)

        logo_label.setFont(self.__font)

        return logo_label_layout

    def __get_login_layout(self, line_edit_width: int, vertical_spacer: int) -> QVBoxLayout:
        
        if not isinstance(line_edit_width, int):
            raise TypeError(type(line_edit_width))
        
        if not isinstance(vertical_spacer, int):
            raise TypeError(type(vertical_spacer))

        login_layout = QVBoxLayout()

        login_label = QLabel(self.__login_widget_qss.login_label_text)

        line_edit_validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("^[a-zA-Z0-9_]*$"))

        login_line_edit = QLineEdit()

        login_line_edit.setMaxLength(25)
        login_line_edit.setValidator(line_edit_validator)

        login_layout.addWidget(login_label, alignment=Qt.AlignmentFlag.AlignCenter)
        login_layout.addSpacerItem(QSpacerItem(0, vertical_spacer))
        login_layout.addWidget(login_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        login_line_edit.setFixedWidth(line_edit_width)
        login_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        login_label.setStyleSheet(self.__login_widget_qss.line_edit_label_qss)
        login_line_edit.setStyleSheet(self.__login_widget_qss.line_edit_qss)

        login_label.setFont(self.__font)
        login_line_edit.setFont(self.__font)

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
        
        password_line_edit.setMaxLength(30)

        password_layout.addWidget(password_label, alignment=Qt.AlignmentFlag.AlignCenter)
        password_layout.addSpacerItem(QSpacerItem(0, vertical_spacer))
        password_layout.addWidget(password_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        password_line_edit.setFixedWidth(line_edit_width)
        password_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        password_label.setStyleSheet(self.__login_widget_qss.line_edit_label_qss)
        password_line_edit.setStyleSheet(self.__login_widget_qss.line_edit_qss)

        password_label.setFont(self.__font)

        return password_layout

    def __get_enter_layout(self) -> QVBoxLayout:

        enter_layout = QVBoxLayout()

        enter_button = QPushButton(self.__login_widget_qss.enter_button_text)
        enter_button.setCursor(Qt.CursorShape.PointingHandCursor)

        enter_layout.addWidget(enter_button, alignment=Qt.AlignmentFlag.AlignCenter)

        enter_button.setStyleSheet(self.__login_widget_qss.enter_button_qss)

        enter_button.setFont(self.__font)

        return enter_layout
    