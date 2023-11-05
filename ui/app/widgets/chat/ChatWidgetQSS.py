from helpers.QSSHelper import QSSHelper
from PyQt6.QtCore import QSize

class ChatWidgetQSS:

    def __init__(self, window_size: QSize) -> None:

        width = window_size.width()
        height = window_size.height()

        self.__contacts_scrollbar_common_qss = """
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{
                """ + QSSHelper.background_color("101010") + """
            }
            QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical{
                """ + QSSHelper.background_color("101010") + """
            }
            QScrollBar::handle:vertical {
                """ + QSSHelper.background("transparent") + """
            }   
        """

        self.__contacts_scrollbar_showed_qss = self.__contacts_scrollbar_common_qss + """
            QScrollBar::vertical {
                """ + QSSHelper.concat(
                        QSSHelper.width(width // 300),
                        QSSHelper.background_color("555555"),
                    ) + \
            """}
        """
        
        self.__contacts_scrollbar_hidden_qss = self.__contacts_scrollbar_common_qss + """
            QScrollBar::vertical {                
                """ + QSSHelper.concat(
                        QSSHelper.width(width // 300),
                        QSSHelper.background_color("101010"),
                    ) + \
            """}
        """

        self.__messages_scrollbar_common_qss = """
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

        self.__messages_scrollbar_showed_qss = self.__contacts_scrollbar_common_qss + """
            QScrollBar::vertical {
                """ + QSSHelper.concat(
                        QSSHelper.width(width // 300),
                        QSSHelper.background_color("555555"),
                    ) + \
            """}
        """
        
        self.__messages_scrollbar_hidden_qss = self.__contacts_scrollbar_common_qss + """
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
                        # QSSHelper.border_side("right", f"{width // 350}px solid #0c0c0c"),
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
    
    @property
    def contacts_scrollbar_hidden_qss(self) -> str:
        return self.__contacts_scrollbar_hidden_qss
    
    @property
    def contacts_scrollbar_showed_qss(self) -> str:
        return self.__contacts_scrollbar_showed_qss
    
    @property
    def messages_scrollbar_hidden_qss(self) -> str:
        return self.__messages_scrollbar_hidden_qss
    
    @property
    def messages_scrollbar_showed_qss(self) -> str:
        return self.__messages_scrollbar_showed_qss
    