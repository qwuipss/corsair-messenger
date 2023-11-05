from .ContactsLayout import ContactsLayout
from .MessagesLayout import MessagesLayout
from .ChatWidgetQSS import ChatWidgetQSS
from PyQt6 import QtCore
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QWidget, QMainWindow

class ChatWidget(QWidget):

    def __init__(self, main_window: QMainWindow) -> None:

        if not isinstance(main_window, QWidget):
            raise TypeError(type(main_window))
        
        super().__init__()

        self.__chat_widget_qss = ChatWidgetQSS(main_window.size())

        self.__contacts_layout = ContactsLayout(self)
        self.__messages_layout = MessagesLayout(main_window, self)

        for i in range(100):

            contact_label = QLabel(f"{i}" * 25)
            
            contact_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
            contact_label.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
            contact_label.setObjectName("contact")

            self.__contacts_layout.add_contact(contact_label)

        for i in range(200):

            message = QLabel(f"w{i}" * 25)

            self.__messages_layout.add_message(message)

            if i % 2:
                message.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            else:
                message.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

            message.setObjectName("message")

        #layout = self.__get_main_layout(self.__contacts_layout, self.__messages_layout)

        #self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)

        self.setStyleSheet(self.__chat_widget_qss.qss)

    def __get_main_layout(self, contacts_layout: QVBoxLayout, messages_layout: QVBoxLayout) -> QHBoxLayout:

        if not isinstance(contacts_layout, QVBoxLayout):
            raise TypeError(type(contacts_layout))
        
        if not isinstance(messages_layout, QVBoxLayout):
            raise TypeError(type(messages_layout))

        layout = QHBoxLayout()

        layout.addLayout(contacts_layout, 2)
        layout.addLayout(messages_layout, 5)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        return layout
