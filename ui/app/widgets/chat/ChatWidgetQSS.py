from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import QSize

class ChatWidgetQSS:

    def __init__(self, window_size: QSize) -> None:

        width = window_size.width()
        height = window_size.height()

        scrollbar_width = str(width // 300)

        self.__scrollbar_common_qss = """
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{
                background: hidden;
            }
            QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical{
                background: #""" + "0c0c0c" + """;
            }
            QScrollBar::handle:vertical {
                background: transparent;
            }   
            """

        self.__scrollbar_showed_qss = self.__scrollbar_common_qss + """
            QScrollBar::vertical {
                width: """ + scrollbar_width + """px;
                background: #""" + "555555" + """;
            }
            """
        
        self.__scrollbar_hidden_qss = self.__scrollbar_common_qss + """
            QScrollBar::vertical {
                width: """ + scrollbar_width + """px;
                background: #""" + "0c0c0c" + """;
            }
            """

        self.__qss = """
            #messageEdit{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width // 70),
                        QSSHelper.background_color("151515"),
                        QSSHelper.border_none(),
                    ) + \
            """}
            #contactsSearch{
                """ + QSSHelper.concat(
                        QSSHelper.font_size(width // 62),
                        QSSHelper.height(height // 13),
                    ) + \
            """}
            #currentContactName{
                """ + QSSHelper.concat(
                        QSSHelper.height(height // 13),
                        QSSHelper.color("ffff00"),
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