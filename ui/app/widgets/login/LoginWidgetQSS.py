from ...SharedQSS import SharedQSS
from helpers.QSSHelper import QSSHelper
from PyQt6.QtWidgets import QMainWindow

class LoginWidgetQSS:

    def __init__(self, main_window: QMainWindow) -> None:

        if not isinstance(main_window, QMainWindow):
            raise TypeError(type(main_window))

        main_window_size = main_window.size()

        width = main_window_size.width()
        
        width_3 = int(width * .3)
        width_02 = int(width * .02)
        width_0088 = int(width * .0088)

        font_weight_550 = 550

        self.__qss = """
            QLabel#logoLabel{
                """ + QSSHelper.concat(
                        QSSHelper.letter_spacing(int(width * .028)),
                        QSSHelper.font_size(int(width * .056)),
                        QSSHelper.font_weight(900),
                    ) + \
            """}
            QLabel#loginLabel, QLabel#passwordLabel{
                """ + QSSHelper.concat(
                        QSSHelper.letter_spacing(int(width * .0038)),
                        QSSHelper.font_size(width_02),
                        QSSHelper.font_weight(font_weight_550),
                    ) + \
            """}
            QLineEdit#loginEdit, QLineEdit#passwordEdit{
                """ + QSSHelper.concat(
                        QSSHelper.color(SharedQSS.COLOR_000000),
                        QSSHelper.background_color(SharedQSS.COLOR_cccccc),
                        QSSHelper.font_size(int(width * .016)),
                        QSSHelper.font_weight(500),
                        QSSHelper.border_radius(width_0088, width_0088, width_0088, width_0088),
                        QSSHelper.width(width_3),
                    ) + \
            """}
            QPushButton#enterButton{
            """ + QSSHelper.concat(
                        QSSHelper.font_size(width_02),
                        QSSHelper.color(SharedQSS.COLOR_555555),
                        QSSHelper.letter_spacing(int(width * .005)),
                        QSSHelper.font_weight(font_weight_550),
                        QSSHelper.border("none"),
                    ) + \
            """}
        """

    @property
    def qss(self) -> str:
        return self.__qss
    