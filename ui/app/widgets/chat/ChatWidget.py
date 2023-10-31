from managers.RegexManager import RegexManager
from .ChatWidgetQSS import ChatWidgetQSS
from PyQt6.QtCore import Qt
from PyQt6 import (
    QtGui, QtCore, 
)
from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem, QScrollArea, QFrame, QPlainTextEdit, QTextEdit,
)

class ChatWidget(QWidget):

    def __init__(self, parent: QWidget, font_id: int) -> None:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        if not isinstance(font_id, int):
            raise TypeError(type(font_id))
        
        super().__init__()

        self.__font = QtGui.QFont(QtGui.QFontDatabase.applicationFontFamilies(font_id)[0])

        self.__chat_widget_qss = ChatWidgetQSS(parent.size())

        messages_layout = self.__get_messages_layout(parent)
        contacts_layout = self.__get_contacts_layout(parent)

        layout = self.__get_main_layout(contacts_layout, messages_layout)

        self.setLayout(layout)

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
            contacts_layout.addWidget(QLabel(f"contact{i}"))

        contacts_extended_layout = QVBoxLayout()
        
        contacts_extended_layout.addWidget(contacts_search)
        contacts_extended_layout.addWidget(contacts_scroll_area)

        contacts_extended_layout.setContentsMargins(0,0,0,0)

        return contacts_extended_layout

    def __get_messages_layout(self, parent: QWidget) -> QVBoxLayout:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        (messages_scroll_area, messages_layout) = self.__get_scroll_area_and_layout(parent)

        for i in range(550):
            al = QLabel()
            al.setText("mes")
            messages_layout.addWidget(al)
            al.setAlignment(Qt.AlignmentFlag.AlignRight)

        messages_extended_layout = QVBoxLayout()

        message_edit = self.__get_message_edit(parent)

        current_contact_name = QLabel("Anonymous")
        current_contact_name.setStyleSheet("border: 1px solid red;")

        messages_extended_layout.addWidget(current_contact_name)
        messages_extended_layout.addWidget(messages_scroll_area)
        messages_extended_layout.addWidget(message_edit)

        height = parent.size().height()

        current_contact_name.setFont(self.__font)
        current_contact_name.setFixedHeight(height // 13)

        return messages_extended_layout

    def __get_scroll_area_and_layout(self, parent: QWidget) -> tuple[QScrollArea, QVBoxLayout]:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        layout = QVBoxLayout()

        widget = QWidget()

        widget.setLayout(layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_area.setWidget(widget)

        scroll_area.enterEvent = lambda _: self.__show_scrollbar(scroll_area)
        scroll_area.leaveEvent = lambda _: self.__hide_scrollbar(scroll_area)

        scroll_area.setStyleSheet(self.__chat_widget_qss.scrollbar_hidden_qss)
        scroll_area.setFrameShape(QFrame.Shape(0))

        return (scroll_area, layout)

    def __get_message_edit(self, parent: QWidget) -> QTextEdit:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        message_edit = QTextEdit()
        
        message_edit_max_height = parent.size().height() // 3

        message_edit.textChanged.connect(lambda: self.__resize_message_edit(message_edit, message_edit_max_height))
        message_edit.setFont(self.__font)
        message_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        message_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        message_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        message_edit.setStyleSheet(self.__chat_widget_qss.message_edit_qss)

        self.__resize_message_edit(message_edit, message_edit_max_height)

        return message_edit

    def __show_scrollbar(self, scroll_area: QScrollArea) -> None:

        if not isinstance(scroll_area, QScrollArea):
            raise TypeError(type(scroll_area))
        
        scroll_area.setStyleSheet(self.__chat_widget_qss.scrollbar_showed_qss)

    def __hide_scrollbar(self, scroll_area: QScrollArea) -> None:

        if not isinstance(scroll_area, QScrollArea):
            raise TypeError(type(scroll_area))

        scroll_area.setStyleSheet(self.__chat_widget_qss.scrollbar_hidden_qss)

    def __get_contacts_search(self, parent: QWidget) -> QLineEdit:
                
        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        contacts_search = QLineEdit()

        line_edit_validator = RegexManager.get_regex_nickname_validator()

        palette = contacts_search.palette()

        palette.setColor(QtGui.QPalette.ColorRole.PlaceholderText, QtGui.QColor(ChatWidgetQSS.SEARCH_PLACEHOLDER_COLOR))

        contacts_search.setFont(self.__font)
        contacts_search.setValidator(line_edit_validator)
        contacts_search.setFixedHeight(parent.size().height() // 13)
        contacts_search.setPlaceholderText(ChatWidgetQSS.CONTACTS_SEARCH_PLACEHOLDER_TEXT)
        contacts_search.setStyleSheet(self.__chat_widget_qss.contacts_search_qss)

        return contacts_search
    
    def __resize_message_edit(self, message_edit: QTextEdit, max_height: int) -> None:

        if not isinstance(message_edit, QTextEdit):
            raise TypeError(type(message_edit))
        
        if not isinstance(max_height, int):
            raise TypeError(type(max_height))

        document_height = int(message_edit.document().size().height())

        if message_edit.size().height() != document_height:
            message_edit.setFixedHeight(min(document_height, max_height))
