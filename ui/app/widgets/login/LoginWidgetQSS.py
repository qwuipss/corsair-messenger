from helpers.QSSHelper import QSSHelper
from ...SharedQSS import SharedQSS
from PyQt6.QtWidgets import QMainWindow

class LoginWidgetQSS:

    def __init__(self, main_window: QMainWindow) -> None:

        if not isinstance(main_window, QMainWindow):
            raise TypeError(type(main_window))

        main_window_size = main_window.size()

        width = main_window_size.width()
        
        line_edit_width = int(width / 3.4)

        font_weight_550 = 550
        width_div_50 = width // 50

        self.__qss = """
            #logoLabel{
                """ + QSSHelper.concat(
                        QSSHelper.letter_spacing(width // 35),
                        QSSHelper.font_size(width // 18),
                        QSSHelper.font_weight(900),
                    ) + \
            """}
            #loginLabel, #passwordLabel{
                """ + QSSHelper.concat(
                        QSSHelper.letter_spacing(width // 260),
                        QSSHelper.font_size(width_div_50),
                        QSSHelper.font_weight(font_weight_550),
                    ) + \
            """}
            #loginEdit, #passwordEdit{
                """ + QSSHelper.concat(
                        QSSHelper.color(SharedQSS.COLOR_000000),
                        QSSHelper.background_color(SharedQSS.COLOR_cccccc),
                        QSSHelper.font_size(width // 62),
                        QSSHelper.font_weight(500),
                        QSSHelper.border_radius(5),
                        QSSHelper.width(line_edit_width),
                    ) + \
            """}
            #enterButton{
            """ + QSSHelper.concat(
                        QSSHelper.font_size(width_div_50),
                        QSSHelper.color(SharedQSS.COLOR_555555),
                        QSSHelper.letter_spacing(width // 200),
                        QSSHelper.font_weight(font_weight_550),
                        QSSHelper.border_none(),
                    ) + \
            """}
        """

    @property
    def qss(self) -> str:
        return self.__qss
    