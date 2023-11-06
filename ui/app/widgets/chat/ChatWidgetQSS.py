from helpers.QSSHelper import QSSHelper
from PyQt6.QtWidgets import QMainWindow

class ChatWidgetQSS:

    def __init__(self, main_window: QMainWindow) -> None:

        if not isinstance(main_window, QMainWindow):
            raise TypeError(type(main_window))

        main_window_size = main_window.size()

        width = main_window_size.width()
        height = main_window_size.height()

        self.__qss = """
            #contactsScrollbarShowed::vertical{
                """ + QSSHelper.background_color("555555") + """
            }
            #contactsScrollbarShowed::sub-page::vertical, #contactsScrollbarShowed::add-page::vertical{
                """ + QSSHelper.background_color("0c0c0c") + """
            }
            #contactsScrollbarHidden::vertical{
                """ + QSSHelper.background_color("0c0c0c") + """
            }
            #contactsScrollbarHidden::sub-page::vertical, #contactsScrollbarHidden::add-page::vertical{
                """ + QSSHelper.background_color("0c0c0c") + """
            }
            #messagesScrollbar::sub-page::vertical, #messagesScrollbar::add-page::vertical{
                """ + QSSHelper.background_color("0c0c0c") + """
            }
            QScrollBar::vertical{
                """ + QSSHelper.concat(
                        QSSHelper.width(width // 300),
                        QSSHelper.background_color("555555"),
                    ) + \
            """}  
            QScrollBar::handle::vertical,
            QScrollBar::up-arrow::vertical, QScrollBar::down-arrow::vertical,
            QScrollBar::add-line::vertical, QScrollBar::sub-line::vertical{
                """ + QSSHelper.background("transparent") +  """
            }
            #messageEdit{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width // 65),
                        QSSHelper.background_color("101010"),
                        QSSHelper.border_none(),
                        QSSHelper.font_weight(100),
                        QSSHelper.color("f2f2f2"),
                        QSSHelper.selection_background_color("555555"),
                    ) + \
            """}
            #contact{
                """ + QSSHelper.concat(
                        QSSHelper.background_color("101010"),
                        QSSHelper.font_size(width // 65),
                        QSSHelper.min_height(width // 23),
                        QSSHelper.padding(0, 0, 0, 5),
                    ) + \
            """}
            #contact::hover{
                """ + QSSHelper.concat(
                        QSSHelper.background_color("141414"),
                    ) + \
            """}
            #message{
                """ + QSSHelper.concat(
                        "border: 1px solid yellow;",
                        QSSHelper.font_size(width // 75),
                        #f"max-width: {width // 3}px;",
                        # QSSHelper.min_height(width // 23),
                        # QSSHelper.padding(0, 0, 0, 5),
                    ) + \
            """}
            #contactsSearch{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width // 62),
                        QSSHelper.min_height(height // 11),
                        QSSHelper.border_none(),
                        QSSHelper.background_color("101010"),
                        QSSHelper.padding(0, 0, 0, width // 150),
                        QSSHelper.font_weight(550),
                        QSSHelper.border_side("right", f"{width // 300}px solid #0c0c0c"),
                    ) + \
            """}
            #currentContactName{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width // 62),
                        QSSHelper.min_height(height // 11),
                        QSSHelper.background_color("101010"),
                        QSSHelper.font_weight(550),
                        QSSHelper.padding(0, 0, 0, width // 150),
                        # QSSHelper.border_side("left", f"{width // 350}px solid #0c0c0c"),
                    ) + \
            """}
        """

    @property
    def qss(self) -> str:
        return self.__qss
    