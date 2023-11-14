from ...SharedQSS import SharedQSS
from helpers.QSSHelper import QSSHelper
from PyQt6.QtWidgets import QMainWindow

class ChatWidgetQSS:

    def __init__(self, main_window: QMainWindow) -> None:

        if not isinstance(main_window, QMainWindow):
            raise TypeError(type(main_window))

        main_window_size = main_window.size()

        width = main_window_size.width()
        height = main_window_size.height()

        width_015 = int(width * .015)
        width_016 = int(width * .016)
        width_0067 = int(width * .0067)
        width_004 = int(width * .004)
        width_005 = int(width * .005)
        width_01 = int(width * .01)
        width_002 = int(width * .002)

        height_1 = int(height * .1)
        height_008 = int(height * .008)

        font_weight_550 = 550

        color_101010 = "101010" 
        color_141414 = "141414"

        self.__qss = """
            QScrollBar::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.background("transparent"),
                        QSSHelper.width(width_004),
                    ) + \
            """}
            QScrollBar::handle::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.background_color("777777"),
                        QSSHelper.min_height(height_008),
                        QSSHelper.border_radius(width_002),
                    ) + \
            """}
            QScrollBar::sub-page::vertical, QScrollBar::add-page::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.background("none"),
                    ) + \
            """}
            QScrollBar::up-arrow::vertical, QScrollBar::down-arrow::vertical,
            QScrollBar::add-line::vertical, QScrollBar::sub-line::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.background("transparent"),
                    ) + \
            """}
            Contact{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_101010),
                        QSSHelper.font_size(width_015),
                        QSSHelper.min_height(int(width * .043)),
                        QSSHelper.padding(0, 0, 0, width_005),
                    ) + \
            """}
            QLabel#currentContactName{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width_016),
                        QSSHelper.min_height(height_1),
                        QSSHelper.background_color(color_101010),
                        QSSHelper.font_weight(font_weight_550),
                        QSSHelper.padding(0, 0, 0, width_0067),
                    ) + \
            """}
            Contact::hover{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_141414),
                    ) + \
            """}
            Contact#selected{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(SharedQSS.COLOR_555555),
                    ) + \
            """}
            Message{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_141414),
                        QSSHelper.border_radius(int(width * .0088)),
                        QSSHelper.font_size(int(width * .013)),
                        QSSHelper.max_width(int(width * .5)),
                        QSSHelper.selection_background_color(SharedQSS.COLOR_555555),
                        QSSHelper.padding(0, width_002, 0, width_002),
                    ) + \
            """}
            QLineEdit#contactsSearch{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width_016),
                        QSSHelper.min_height(height_1),
                        QSSHelper.border("none"),
                        QSSHelper.background_color(color_101010),
                        QSSHelper.padding(0, 0, 0, width_0067),
                        QSSHelper.font_weight(font_weight_550),
                        QSSHelper.selection_background_color(SharedQSS.COLOR_555555),
                        QSSHelper.margin_side("right", f"{width_004}px solid #{SharedQSS.COLOR_0c0c0c}"),
                    ) + \
            """}
            MessageEdit{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width_015),
                        QSSHelper.background_color(color_101010),
                        QSSHelper.border("none"),
                        QSSHelper.font_weight(100),
                        QSSHelper.color(SharedQSS.COLOR_f2f2f2),
                        QSSHelper.selection_background_color(SharedQSS.COLOR_555555),
                        QSSHelper.padding(width_005, width_01, width_005, width_01),
                    ) + \
            """}
        """

    @property
    def qss(self) -> str:
        return self.__qss
    