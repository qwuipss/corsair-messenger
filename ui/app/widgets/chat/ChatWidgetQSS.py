from ...SharedQSS import ChatWidgetSharedQSS
from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import QSize

class ChatWidgetQSS:

    def __init__(self, window_size: QSize) -> None:

        width = window_size.width()

        scrollbar_width = str(width // 300)

        self.__scrollbar_common_qss = """
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{
                background: #""" + ChatWidgetSharedQSS.BACKGROUND_COLOR + """;
            }
            QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical{
                background: #""" + ChatWidgetSharedQSS.BACKGROUND_COLOR + """;
            }
            QScrollBar::handle:vertical {
                background: transparent;
            }   
            """

        self.__scrollbar_showed_qss = self.__scrollbar_common_qss + """
            QScrollBar::vertical {
                width: """ + scrollbar_width + """px;
                background: #""" + ChatWidgetSharedQSS.SCROLLBAR_SHOWED_COLOR + """;
            }
            """
        
        self.__scrollbar_hidden_qss = self.__scrollbar_common_qss + """
            QScrollBar::vertical {
                width: """ + scrollbar_width + """px;
                background: #""" + ChatWidgetSharedQSS.BACKGROUND_COLOR + """;
            }
            """
        
        self.__contacts_search_placeholder = "Search"    
        self.__contacts_search_qss = ChatWidgetQSS.__get_contacts_search_qss(window_size)

    @property
    def scrollbar_showed_qss(self) -> str:
        return self.__scrollbar_showed_qss
    
    @property
    def scrollbar_hidden_qss(self) -> str:
        return self.__scrollbar_hidden_qss

    @property
    def contacts_search_placeholder(self) -> str:
        return self.__contacts_search_placeholder
    
    @property
    def contacts_search_qss(self) -> str:
        return self.__contacts_search_qss

    @staticmethod
    def __get_contacts_search_qss(window_size: QSize) -> str:
        
        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))

        return QSSHelper.concat(
            QSSHelper.font_size(window_size.width() // 62),
        )