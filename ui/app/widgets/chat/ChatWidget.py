from managers.RegexManager import RegexManager
from ...gui.MessageEdit import MessageEdit
from .ChatWidgetQSS import ChatWidgetQSS
from PyQt6.QtCore import Qt
from PyQt6 import (
    QtGui, QtCore, 
)
from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem, QScrollArea, QFrame, QPlainTextEdit, QTextEdit, 
)

class ChatWidget(QWidget):

    def __init__(self, parent: QWidget) -> None:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        super().__init__()

        self.__chat_widget_qss = ChatWidgetQSS(parent.size())

        contacts_layout = self.__get_contacts_layout(parent)
        messages_layout = self.__get_messages_layout(parent)

        layout = self.__get_main_layout(contacts_layout, messages_layout)

        self.setLayout(layout)
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

    def __get_contacts_layout(self, parent: QWidget) -> QVBoxLayout:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        (contacts_scroll_area, contacts_layout) = self.__get_scroll_area_and_layout(parent)
        contacts_search = self.__get_contacts_search(parent)

        for i in range(500):

            contact_label = QLabel(f"w" * 25)
            
            contact_label.setAlignment(Qt.AlignmentFlag.AlignTop)
            contact_label.setCursor(Qt.CursorShape.PointingHandCursor)
            contact_label.setObjectName("contact")
            
            contacts_layout.addWidget(contact_label)

        contacts_extended_layout = QVBoxLayout()
        
        contacts_extended_layout.addWidget(contacts_search)
        contacts_extended_layout.addWidget(contacts_scroll_area)

        contacts_layout.setSpacing(0)
        contacts_layout.setContentsMargins(0, 0, 0, 0)

        return contacts_extended_layout

    def __get_messages_layout(self, parent: QWidget) -> QVBoxLayout:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        (messages_scroll_area, messages_layout) = self.__get_scroll_area_and_layout(parent)

        for i in range(150):

            message = QLabel(f"w{i}" * 25)

            message_layout = QVBoxLayout()

            messages_layout.addWidget(message)

            if i % 2:
                message.setAlignment(Qt.AlignmentFlag.AlignRight)
                # s = message.styleSheet()
                # message.setStyleSheet("padding: 0 0 0 0;")
            else:
                message.setAlignment(Qt.AlignmentFlag.AlignLeft)

            # message.setFixedWidth(300)
            message.setObjectName("message")
            
            messages_layout.addLayout(message_layout)

        messages_extended_layout = QVBoxLayout()

        message_edit = self.__get_message_edit(parent)

        current_contact_name = QLabel("Anonymous")

        current_contact_name.setObjectName("currentContactName")

        messages_extended_layout.addWidget(current_contact_name)
        messages_extended_layout.addWidget(messages_scroll_area)
        messages_extended_layout.addWidget(message_edit)

        return messages_extended_layout

    def __get_scroll_area_and_layout(self, parent: QWidget) -> tuple[QScrollArea, QVBoxLayout]:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        layout = QVBoxLayout()

        widget = QWidget(self)

        widget.setLayout(layout)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_area.setWidget(widget)

        scroll_area.enterEvent = lambda _: self.__show_scrollbar(scroll_area)
        scroll_area.leaveEvent = lambda _: self.__hide_scrollbar(scroll_area)

        scroll_area.setStyleSheet(self.__chat_widget_qss.contacts_scrollbar_hidden_qss)
        scroll_area.setFrameShape(QFrame.Shape(0))

        return (scroll_area, layout)

    def __get_message_edit(self, parent: QWidget) -> QTextEdit:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        message_edit_max_height = parent.size().height() // 3
        
        message_edit = MessageEdit(self, message_edit_max_height)

        message_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        message_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        message_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        message_edit.setObjectName("messageEdit")

        return message_edit

    def __show_scrollbar(self, scroll_area: QScrollArea) -> None:

        if not isinstance(scroll_area, QScrollArea):
            raise TypeError(type(scroll_area))
        
        scroll_area.setStyleSheet(self.__chat_widget_qss.contacts_scrollbar_showed_qss)

    def __hide_scrollbar(self, scroll_area: QScrollArea) -> None:

        if not isinstance(scroll_area, QScrollArea):
            raise TypeError(type(scroll_area))

        scroll_area.setStyleSheet(self.__chat_widget_qss.contacts_scrollbar_hidden_qss)

    def __get_contacts_search(self, parent: QWidget) -> QLineEdit:
                
        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        contacts_search = QLineEdit(self)

        line_edit_validator = RegexManager.get_regex_nickname_validator()

        placeholder_palette = contacts_search.palette()
        placeholder_palette.setColor(QtGui.QPalette.ColorRole.PlaceholderText, QtGui.QColor("#555555"))  

        contacts_search.setPalette(placeholder_palette)
        contacts_search.setValidator(line_edit_validator)
        contacts_search.setPlaceholderText("Search")
        contacts_search.setObjectName("contactsSearch")

        return contacts_search
    