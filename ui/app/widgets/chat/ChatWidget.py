from .ContactsWidget import ContactsWidget
from .MessagesWidget import MessagesWidget
from .ChatWidgetQSS import ChatWidgetQSS
from .Message import Message
from PyQt6 import QtCore
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QWidget, QMainWindow

class ChatWidget(QWidget):

    def __init__(self, main_window: QMainWindow) -> None:

        if not isinstance(main_window, QWidget):
            raise TypeError(type(main_window))
        
        super().__init__(main_window)

        self.__chat_widget_qss = ChatWidgetQSS(main_window)

        self.__contacts_widget = ContactsWidget(self)
        self.__messages_widget = MessagesWidget(main_window, self)

        # ---------------
        for i in range(100):

            contact_label = QLabel(f"{i}" * 25)
            
            contact_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            contact_label.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            contact_label.setObjectName("contact")

            self.__contacts_widget.add_contact(contact_label)

        # for i in range(150):

            message = Message("1111111111111112222222222222  33333333333333333333333333333333333333333333 4444444444 44444444444 11111111111111122222222222222222222222333333333333333333333333444444444444444444555555555555555566666666666666667777777777777777777777777777777777777777777777777777777777777777777777777777777777777777788888888888888888888888", self)
            self.__messages_widget.add_message(message, i % 2)
            message = Message("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111112", self)
            self.__messages_widget.add_message(message, i % 2)
            message = Message("123213123", self)
            self.__messages_widget.add_message(message, i % 2)
            message = Message("1111111111111112222222222222222222222233333333333333333333333344444444444444444455555555555555556666666666666666", self)
            self.__messages_widget.add_message(message, i % 2)
            message = Message("1                                                                                                            22222222222222222223333333333333333333333333333333333334444 55555555555555555555555555555556", self)
            self.__messages_widget.add_message(message, i % 2)
            
        # -------------

        layout = self.__get_main_layout()

        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)

        self.setStyleSheet(self.__chat_widget_qss.qss)

    def __get_main_layout(self) -> QHBoxLayout:

        layout = QHBoxLayout()

        contacts_layout = self.__get_contacts_layout()
        messages_layout = self.__get_messages_layout()

        layout.addLayout(contacts_layout, 2)
        layout.addLayout(messages_layout, 5)

        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        return layout

    def __get_contacts_layout(self) -> QVBoxLayout:

        contacts_layout = QVBoxLayout()

        self.__contacts_widget.contacts_scrollarea.layout.setSpacing(0)
        self.__contacts_widget.contacts_scrollarea.layout.setContentsMargins(0, 0, 0, 0)

        contacts_layout.addWidget(self.__contacts_widget.contacts_search)
        contacts_layout.addWidget(self.__contacts_widget.contacts_scrollarea)
        contacts_layout.setSpacing(0)
        contacts_layout.setContentsMargins(0, 0, 0, 0)

        return contacts_layout
    
    def __get_messages_layout(self) -> QVBoxLayout:

        messages_layout = QVBoxLayout()
        
        messages_layout.addWidget(self.__messages_widget.current_contact_name)
        messages_layout.addWidget(self.__messages_widget.messages_scrollarea)
        messages_layout.addWidget(self.__messages_widget.message_edit)

        return messages_layout
    