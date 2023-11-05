from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import QSize

class ChatWidgetQSS:

    def __init__(self, window_size: QSize) -> None:

        width = window_size.width()
        height = window_size.height()

        self.__scrollbar_common_qss = """
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{
                """ + QSSHelper.background_color("0c0c0c") + """
            }
            QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical{
                """ + QSSHelper.background_color("0c0c0c") + """
            }
            QScrollBar::handle:vertical {
                """ + QSSHelper.background("transparent") + """
            }   
        """

        self.__scrollbar_showed_qss = self.__scrollbar_common_qss + """
            QScrollBar::vertical {
                """ + QSSHelper.concat(
                        QSSHelper.width(width // 300),
                        QSSHelper.background_color("555555"),
                    ) + \
            """}
        """
        
        self.__scrollbar_hidden_qss = self.__scrollbar_common_qss + """
            QScrollBar::vertical {                
                """ + QSSHelper.concat(
                        QSSHelper.width(width // 300),
                        QSSHelper.background_color("0c0c0c"),
                    ) + \
            """}
        """

        self.__qss = """
            #messageEdit{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width // 65),
                        QSSHelper.background_color("0e0e0e"),
                        QSSHelper.border_none(),
                        QSSHelper.font_weight(100),
                        QSSHelper.color("f2f2f2"),
                        QSSHelper.selection_background_color("555555"),
                    ) + \
            """}
            #contact{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width // 65),
                        QSSHelper.min_height(width // 23),
                        QSSHelper.padding(0, 0, 0, 5),
                    ) + \
            """}
            #contact::hover{
                """ + QSSHelper.concat(
                        QSSHelper.background_color("111111"),
                    ) + \
            """}
            #contactsSearch{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width // 62),
                        QSSHelper.min_height(height // 11),
                        QSSHelper.border_none(),
                        QSSHelper.background_color("0e0e0e"),
                        QSSHelper.border_side("right", f"{width // 250}px solid #0c0c0c"),
                        QSSHelper.padding(0, 0, 0, width // 150),
                        QSSHelper.font_weight(550),
                    ) + \
            """}
            #currentContactName{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width // 62),
                        QSSHelper.min_height(height // 11),
                        QSSHelper.background_color("0e0e0e"),
                        QSSHelper.font_weight(550),
                        QSSHelper.padding(0, 0, 0, width // 150)
                    ) + \
            """}
        """

    @property
    def qss(self) -> str:
        return self.__qss
    
    @property
    def scrollbar_hidden_qss(self) -> str:
        return self.__scrollbar_hidden_qss
    
    @property
    def scrollbar_showed_qss(self) -> str:
        return self.__scrollbar_showed_qss
    