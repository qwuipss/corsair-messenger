from ...SharedQSS import LoginWidgetSharedQSS
from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import QSize

class LoginWidgetQSS:

    def __init__(self, window_size: QSize) -> None:
        
        self.__logo_label_text = "CORSAIR"
        self.__logo_label_qss = LoginWidgetQSS.__get_logo_label_qss(window_size)

        self.__login_label_text = "Login"
        self.__password_label_text = "Password"
        
        self.__line_edit_qss = LoginWidgetQSS.__get_line_edit_qss(window_size)
        self.__line_edit_label_qss = LoginWidgetQSS.__get_line_edit_label_qss(window_size)

        self.__enter_button_text = "Enter"
        self.__enter_button_qss = LoginWidgetQSS.__get_enter_button_qss(window_size)

    @property
    def logo_label_text(self) -> str:
        return self.__logo_label_text
    
    @property
    def logo_label_qss(self) -> str:
        return self.__logo_label_qss

    @property
    def login_label_text(self) -> str:
        return self.__login_label_text

    @property
    def password_label_text(self) -> str:
        return self.__password_label_text
    
    @property
    def line_edit_label_qss(self) -> str:
        return self.__line_edit_label_qss

    @property
    def line_edit_qss(self) -> str:
        return self.__line_edit_qss
    
    @property
    def enter_button_text(self) -> str:
        return self.__enter_button_text
    
    @property
    def enter_button_qss(self) -> str:
        return self.__enter_button_qss

    @staticmethod
    def __get_logo_label_qss(window_size: QSize) -> str:

        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))

        width = window_size.width()

        qss = QSSHelper.concat(
            QSSHelper.letter_spacing(int(width / 35)),
            QSSHelper.font_size(int(width / 18)),
            QSSHelper.font_weight(900),
        )

        return qss
    
    @staticmethod
    def __get_line_edit_label_qss(window_size: QSize) -> str:

        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))
        
        width = window_size.width()

        qss = QSSHelper.concat(
            QSSHelper.letter_spacing(int(width / 260)),
            QSSHelper.font_size(int(width / 50)),
            QSSHelper.font_weight(550),
        )

        return qss

    @staticmethod
    def __get_line_edit_qss(window_size: QSize) -> str:

        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))
        
        width = window_size.width()

        qss = QSSHelper.concat(
            QSSHelper.color(LoginWidgetSharedQSS.LINE_EDIT_COLOR),
            QSSHelper.background_color(LoginWidgetSharedQSS.LINE_EDIT_BACKGROUND_COLOR),
            QSSHelper.font_size(int(width / 62)),
            QSSHelper.font_weight(500),
            QSSHelper.border_radius(5),
        )

        return qss
    
    @staticmethod
    def __get_enter_button_qss(window_size: QSize) -> str:

        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))
        
        width = window_size.width()

        qss = QSSHelper.concat(
            QSSHelper.font_size(int(width / 50)),
            QSSHelper.color(LoginWidgetSharedQSS.ENTER_BUTTON_TEXT_COLOR),
            QSSHelper.letter_spacing(int(width / 200)),
            QSSHelper.font_weight(550),
            QSSHelper.border_none(),
        )

        return qss    
