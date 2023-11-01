from helpers.QSSHelper import QSSHelper

class MainWindowQSS:

    def __init__(self) -> None:
        
        self.__qss = """
            QWidget{
                """ + QSSHelper.concat(
                        QSSHelper.background_color("0c0c0c"),
                        QSSHelper.color("f2f2f2"),
                        QSSHelper.font_family("Kanit"),
                        QSSHelper.font_weight(400),
                ) + \
            """}
        """

    @property
    def qss(self) -> str:
        return self.__qss
    