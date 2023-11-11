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
            QScrollBar::vertical{
                width:4px;   
                background: transparent;
            }            
            QScrollBar::handle::vertical{
                background-color: #555555;
                border-radius: 2px;
                min-height: 8px;
            }     
            QScrollBar::sub-page::vertical, QScrollBar::add-page::vertical{
                background: none;
            }
            QScrollBar::up-arrow::vertical, QScrollBar::down-arrow::vertical,
            QScrollBar::add-line::vertical, QScrollBar::sub-line::vertical{
                background:transparent;
            }
            MessageEdit{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width_div_65),
                        QSSHelper.background_color(color_101010),
                        QSSHelper.border_none(),
                        QSSHelper.font_weight(100),
                        QSSHelper.color(SharedQSS.COLOR_f2f2f2),
                        QSSHelper.selection_background_color(SharedQSS.COLOR_555555),
                        "padding: 5px 10px 5px 10px;",
                    ) + \
            """}
            QLabel#contact{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_101010),
                        QSSHelper.font_size(width_div_65),
                        QSSHelper.min_height(width // 23),
                        QSSHelper.padding(0, 0, 0, 5),
                    ) + \
            """}
            QLabel#contact::hover{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_141414),
                    ) + \
            """}
            Message{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_141414),
                        QSSHelper.border_radius(7),
                        QSSHelper.font_size(width // 75),
                        QSSHelper.selection_background_color(SharedQSS.COLOR_555555),
                        QSSHelper.max_width(width // 2),
                    ) + \
            """}
            QLineEdit#contactsSearch{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width_div_62),
                        QSSHelper.min_height(height_div_11),
                        QSSHelper.border_none(),
                        QSSHelper.background_color(color_101010),
                        QSSHelper.padding(0, 0, 0, width_div_150),
                        QSSHelper.font_weight(font_weight_550),
                        QSSHelper.selection_background_color(SharedQSS.COLOR_555555),
                        
                        "margin-right: 4px solid #0c0c0c"
                    ) + \
            """}
            QLabel#currentContactName{
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
    