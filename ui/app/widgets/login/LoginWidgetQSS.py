from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import QSize

class LoginWidgetQSS:

    def __init__(self, screen_size: QSize) -> None:
        
        self.__logo_label_text = "CORSAIR"
        self.__logo_label_qss = LoginWidgetQSS.__get_logo_label_qss(screen_size)

        self.__login_label_text = "Login"
        self.__login_label_qss = self.__get_login_label_qss(screen_size)

    @property
    def logo_label_text(self) -> str:
        return str(self.__logo_label_text)

    @property
    def login_label_text(self) -> str:
        return str(self.__login_label_text)

    @property
    def login_label_qss(self) -> str:
        return str(self.__login_label_qss)

    @property
    def logo_label_qss(self) -> str:
        return str(self.__logo_label_qss)
    
    @staticmethod
    def __get_logo_label_qss(screen_size: QSize) -> str:

        if not isinstance(screen_size, QSize):
            raise TypeError(type(screen_size))

        width = screen_size.width()

        qss = QSSHelper.concat(
            QSSHelper.letter_spacing(int(width / 60)),
            QSSHelper.font_size(int(width / 30)),
            QSSHelper.font_weight(900),
        )

        return qss
    
    @staticmethod
    def __get_login_label_qss(screen_size: QSize) -> str:

        if not isinstance(screen_size, QSize):
            raise TypeError(type(screen_size))
        
        width = screen_size.width()

        qss = QSSHelper.concat(
            QSSHelper.letter_spacing(int(width / 350)),
            QSSHelper.font_size(int(width / 80)),
            QSSHelper.font_weight(500),         
        )

        return qss
