from helpers.QSSHelper import QSSHelper
from ...SharedQSS import SharedQSS
from PyQt6.QtWidgets import QMainWindow

class ChatWidgetQSS:

    def __init__(self, main_window: QMainWindow) -> None:

        if not isinstance(main_window, QMainWindow):
            raise TypeError(type(main_window))

        main_window_size = main_window.size()

        width = main_window_size.width()
        height = main_window_size.height()

        width_div_65 = width // 65
        width_div_62 = width // 62
        width_div_150 = width // 150
        width_div_300 = width // 300

        height_div_11 = height // 11

        font_weight_550 = 550

        color_101010 = "101010" 
        color_141414 = "141414"

        self.__qss = """
            #contactsScrollbarShowed::vertical{
                """ + QSSHelper.background_color(SharedQSS.COLOR_555555) + """
            }
            #contactsScrollbarShowed::sub-page::vertical, #contactsScrollbarShowed::add-page::vertical{
                """ + QSSHelper.background_color(SharedQSS.COLOR_0c0c0c) + """
            }
            #contactsScrollbarHidden::vertical{
                """ + QSSHelper.background_color(SharedQSS.COLOR_0c0c0c) + """
            }
            #contactsScrollbarHidden::sub-page::vertical, #contactsScrollbarHidden::add-page::vertical{
                """ + QSSHelper.background_color(SharedQSS.COLOR_0c0c0c) + """
            }
            #messagesScrollbar::sub-page::vertical, #messagesScrollbar::add-page::vertical{
                """ + QSSHelper.background_color(SharedQSS.COLOR_0c0c0c) + """
            }
            QScrollBar::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.width(width_div_300),
                        QSSHelper.background_color(SharedQSS.COLOR_555555),
                    ) + \
            """}  
            QScrollBar::handle::vertical,
            QScrollBar::up-arrow::vertical, QScrollBar::down-arrow::vertical,
            QScrollBar::add-line::vertical, QScrollBar::sub-line::vertical{
                """ + QSSHelper.background("transparent") +  """
            }
            #messageEdit{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width_div_65),
                        QSSHelper.background_color(color_101010),
                        QSSHelper.border_none(),
                        QSSHelper.font_weight(100),
                        QSSHelper.color(SharedQSS.COLOR_f2f2f2),
                        QSSHelper.selection_background_color(SharedQSS.COLOR_555555),
                    ) + \
            """}
            #contact{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_101010),
                        QSSHelper.font_size(width_div_65),
                        QSSHelper.min_height(width // 23),
                        QSSHelper.padding(0, 0, 0, 5),
                    ) + \
            """}
            #contact::hover{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_141414),
                    ) + \
            """}
            #message{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_141414),
                        QSSHelper.border_radius(7),
                        QSSHelper.font_size(width // 75),
                        QSSHelper.selection_background_color(SharedQSS.COLOR_555555),
                        QSSHelper.max_width(width // 2),
                    ) + \
            """}
            #contactsSearch{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width_div_62),
                        QSSHelper.min_height(height_div_11),
                        QSSHelper.border_none(),
                        QSSHelper.background_color(color_101010),
                        QSSHelper.padding(0, 0, 0, width_div_150),
                        QSSHelper.font_weight(font_weight_550),
                        QSSHelper.border_side("right", f"{width_div_300}px solid #{SharedQSS.COLOR_0c0c0c}"),
                        QSSHelper.selection_background_color(SharedQSS.COLOR_555555),
                    ) + \
            """}
            #currentContactName{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width_div_62),
                        QSSHelper.min_height(height_div_11),
                        QSSHelper.background_color(color_101010),
                        QSSHelper.font_weight(font_weight_550),
                        QSSHelper.padding(0, 0, 0, width_div_150),
                    ) + \
            """}
        """

    @property
    def qss(self) -> str:
        return self.__qss
    