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
        width_0088 = int(width * .0088)
        width_003 = int(width * .003)
        width_0059 = int(width * .0059)

        height_1 = int(height * .1)
        height_008 = int(height * .008)

        font_weight_550 = 550

        color_101010 = "101010" 
        color_141414 = "141414"
        color_777777 = "777777"

        layouts_margin = QSSHelper.margin_side("left", width_004)

        self.__qss = """
            QScrollBar::handle::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.min_height(height_008),
                        QSSHelper.border_radius(width_002, width_002, width_002, width_002),
                    ) + \
            """}
            QScrollBar#messagesScrollbarShowed::vertical, QScrollBar#messagesScrollbarHidden::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.width(width_004 + width_003),
                    ) + \
            """}
            QScrollBar#messagesScrollbarShowed::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_101010),
                        QSSHelper.margin(width_0059, width_003, width_0059, 0),
                    ) + \
            """}
            QScrollBar#messagesScrollbarShowed::handle::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_777777),
                    ) + \
            """}            
            QScrollBar#contactsScrollbarShowed::handle::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_777777),
                    ) + \
            """}
            QScrollBar#contactsScrollbarShowed::vertical, QScrollBar#contactsScrollbarHidden::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.width(width_004),
                        QSSHelper.background_color(color_101010),
                        QSSHelper.padding(width_0059, 0, width_0059, 0),
                    ) + \
            """}
            QScrollBar#messagesScrollbarHidden::vertical,
            QScrollBar#messagesScrollbarHidden::handle::vertical,
            QScrollBar::sub-page::vertical, QScrollBar::add-page::vertical,
            QScrollBar::up-arrow::vertical, QScrollBar::down-arrow::vertical,
            QScrollBar::add-line::vertical, QScrollBar::sub-line::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.background("transparent"),
                    ) + \
            """}
            Scrollarea#messagesScrollarea{
                """ + QSSHelper.concat(
                        layouts_margin,
                    ) + \
            """}
            QWidget#contactsScrollwidget{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_101010),
                    ) + \
            """}
            Contact{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_101010),
                        QSSHelper.font_size(width_015),
                        QSSHelper.padding(0, 0, 0, width_005),
                        QSSHelper.margin_side("right", width_002),
                        QSSHelper.border_radius(width_0088, width_0088, 0, 0),
                    ) + \
            """}
            LastMessage{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_101010),
                        QSSHelper.font_size(int(width *.0127)),
                        QSSHelper.padding(0, 0, 0, width_005),
                        QSSHelper.margin_side("right", width_002),
                        QSSHelper.color("595959"),
                        QSSHelper.border_radius(0, 0, width_0088, width_0088),
                    ) + \
            """}
            Contact#hovered, LastMessage#hovered{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_141414),
                    ) + \
            """}
            Contact#selected, LastMessage#selected{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(SharedQSS.COLOR_555555),
                    ) + \
            """}
            LastMessage#selected{
                """ + QSSHelper.concat(
                        QSSHelper.color(SharedQSS.COLOR_f2f2f2),
                    ) + \
            """}
            Message{
                """ + QSSHelper.concat(
                        QSSHelper.background_color(color_141414),
                        QSSHelper.border_radius(width_0088, width_0088, width_0088, width_0088),
                        QSSHelper.font_size(int(width * .013)),
                        QSSHelper.max_width(int(width * .5)),
                        QSSHelper.selection_background_color(SharedQSS.COLOR_555555),
                        QSSHelper.padding(0, width_002, 0, width_002),
                    ) + \
            """}
            QLabel#currentContactName{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width_016),
                        QSSHelper.min_height(height_1),
                        QSSHelper.background_color(color_101010),
                        QSSHelper.font_weight(font_weight_550),
                        QSSHelper.padding(0, 0, 0, width_0067),
                        layouts_margin,
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
                        layouts_margin,
                    ) + \
            """}
        """

    @property
    def qss(self) -> str:
        return self.__qss
    