from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import QSize

class ChatWidgetQSS:

    CONTACTS_SEARCH_PLACEHOLDER_TEXT = "Search"

    SEARCH_COLOR = "f2f2f2"

    SEARCH_PLACEHOLDER_COLOR = "555555"

    MESSAGE_EDIT_COLOR = "f2f2f2"

    MESSAGE_EDIT_BACKGROUND_COLOR = "151515"

    MESSAGE_SCROLLAREA_BACKGROUND_COLOR = "0c0c0c"

    SCROLLBAR_COLOR = "555555"

    def __init__(self, window_size: QSize) -> None:

        width = window_size.width()

        scrollbar_width = str(width // 300)

        self.__scrollbar_common_qss = """
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{
                background: hidden;
            }
            QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical{
                background: #""" + ChatWidgetQSS.MESSAGE_SCROLLAREA_BACKGROUND_COLOR + """;
            }
            QScrollBar::handle:vertical {
                background: transparent;
            }   
            """

        self.__scrollbar_showed_qss = self.__scrollbar_common_qss + """
            QScrollBar::vertical {
                width: """ + scrollbar_width + """px;
                background: #""" + ChatWidgetQSS.SCROLLBAR_COLOR + """;
            }
            """
        
        self.__scrollbar_hidden_qss = self.__scrollbar_common_qss + """
            QScrollBar::vertical {
                width: """ + scrollbar_width + """px;
                background: #""" + ChatWidgetQSS.MESSAGE_SCROLLAREA_BACKGROUND_COLOR + """;
            }
            """
         
        self.__contacts_search_qss = ChatWidgetQSS.__get_contacts_search_qss(window_size)

        self.__message_edit_qss = ChatWidgetQSS.__get_message_edit_qss(window_size)

    @property
    def message_edit_qss(self) -> str:
        return self.__message_edit_qss

    @property
    def scrollbar_showed_qss(self) -> str:
        return self.__scrollbar_showed_qss
    
    @property
    def scrollbar_hidden_qss(self) -> str:
        return self.__scrollbar_hidden_qss
    
    @property
    def contacts_search_qss(self) -> str:
        return self.__contacts_search_qss

    @staticmethod
    def __get_contacts_search_qss(window_size: QSize) -> str:
        
        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))

        return QSSHelper.concat(
            QSSHelper.font_size(window_size.width() // 62),
            QSSHelper.color(ChatWidgetQSS.SEARCH_COLOR),
        )
    
    @staticmethod
    def __get_message_edit_qss(window_size: QSize) -> str:
        
        if not isinstance(window_size, QSize):
            raise TypeError(type(window_size))

        return QSSHelper.concat(
            QSSHelper.font_size(window_size.width() // 70),
            QSSHelper.color(ChatWidgetQSS.MESSAGE_EDIT_COLOR),
            QSSHelper.background_color(ChatWidgetQSS.MESSAGE_EDIT_BACKGROUND_COLOR),
            QSSHelper.border_none(),
            QSSHelper.font_weight(400),
        )