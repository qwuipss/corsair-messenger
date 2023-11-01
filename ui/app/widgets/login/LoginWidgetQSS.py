from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import QSize

class LoginWidgetQSS:

    def __init__(self, window_size: QSize) -> None:

        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))
        
        width = window_size.width()
        
        line_edit_width = int(width / 3.4)

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
                        QSSHelper.font_size(width // 50),
                        QSSHelper.font_weight(550),
                    ) + \
            """}
            #loginEdit, #passwordEdit{
                """ + QSSHelper.concat(
                        QSSHelper.color("000000"),
                        QSSHelper.background_color("cccccc"),
                        QSSHelper.font_size(width // 62),
                        QSSHelper.font_weight(500),
                        QSSHelper.border_radius(5),
                        QSSHelper.width(line_edit_width),
                    ) + \
            """}
            #enterButton{
            """ + QSSHelper.concat(
                        QSSHelper.font_size(width // 50),
                        QSSHelper.color("555555"),
                        QSSHelper.letter_spacing(width // 200),
                        QSSHelper.font_weight(550),
                        QSSHelper.border_none(),
                    ) + \
            """}
        """

    @property
    def qss(self) -> str:
        return self.__qss
    