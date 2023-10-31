from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import QSize

class LoginWidgetQSS:

    LOGO_LABEL_TEXT = "CORSAIR"

    LOGIN_LABEL_TEXT = "Login"
    
    PASSWORD_LABEL_TEXT = "Password"
    
    ENTER_BUTTON_LABEL_TEXT = "Enter"

    LOGO_LABEL_COLOR = "f2f2f2"

    FORM_LABEL_COLOR = "000000"

    FORM_EDIT_BACKGROUND_COLOR = "cccccc"

    ENTER_BUTTON_COLOR = "555555"

    def __init__(self, window_size: QSize) -> None:
        
        self.__logo_label_qss = LoginWidgetQSS.__get_logo_label_qss(window_size)
        
        self.__line_edit_qss = LoginWidgetQSS.__get_line_edit_qss(window_size)
        self.__line_edit_label_qss = LoginWidgetQSS.__get_line_edit_label_qss(window_size)
        self.__enter_button_qss = LoginWidgetQSS.__get_enter_button_qss(window_size)

    @property
    def logo_label_qss(self) -> str:
        return self.__logo_label_qss

    @property
    def line_edit_label_qss(self) -> str:
        return self.__line_edit_label_qss

    @property
    def line_edit_qss(self) -> str:
        return self.__line_edit_qss
    
    @property
    def enter_button_qss(self) -> str:
        return self.__enter_button_qss

    @staticmethod
    def __get_logo_label_qss(window_size: QSize) -> str:

        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))

        width = window_size.width()

        qss = QSSHelper.concat(
            QSSHelper.letter_spacing(width // 35),
            QSSHelper.font_size(width // 18),
            QSSHelper.font_weight(900),
        )

        return qss
    
    @staticmethod
    def __get_line_edit_label_qss(window_size: QSize) -> str:

        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))
        
        width = window_size.width()

        qss = QSSHelper.concat(
            QSSHelper.letter_spacing(width // 260),
            QSSHelper.font_size(width // 50),
            QSSHelper.font_weight(550),
        )

        return qss

    @staticmethod
    def __get_line_edit_qss(window_size: QSize) -> str:

        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))
        
        width = window_size.width()

        qss = QSSHelper.concat(
            QSSHelper.color(LoginWidgetQSS.FORM_LABEL_COLOR),
            QSSHelper.background_color(LoginWidgetQSS.FORM_EDIT_BACKGROUND_COLOR),
            QSSHelper.font_size(width // 62),
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
            QSSHelper.font_size(width // 50),
            QSSHelper.color(LoginWidgetQSS.ENTER_BUTTON_COLOR),
            QSSHelper.letter_spacing(width // 200),
            QSSHelper.font_weight(550),
            QSSHelper.border_none(),
        )

        return qss    
