#from .ChatWidgetQSS import ChatWidgetQSS
from PyQt6 import QtGui
from PyQt6 import QtCore
from PyQt6.QtCore import (
    Qt, QSize, 
)
from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem, QScrollArea, QGridLayout, QMessageBox,
)

class ChatWidget(QWidget):

    def __init__(self, parent: QWidget, font_id: int) -> None:

        #demo

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        if not isinstance(font_id, int):
            raise TypeError(type(font_id))
        
        super().__init__()

        contacts_scroll_area = QScrollArea()
        contacts_scroll_area.setWidgetResizable(True)

        messages_scroll_area = QScrollArea()
        messages_scroll_area.setWidgetResizable(True)

        contacts_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        contacts_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        messages_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        messages_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        contacts_layout = QVBoxLayout()
        contacts_widget = QWidget()
        contacts_widget.setLayout(contacts_layout)

        messages_layout = QVBoxLayout()
        messages_widget = QWidget()
        messages_widget.setLayout(messages_layout)

        for i in range(50):
            contacts_layout.addWidget(QLabel("contact"))

        for i in range(70):
            messages_layout.addWidget(QLabel("message"))

        contacts_scroll_area.setWidget(contacts_widget)
        messages_scroll_area.setWidget(messages_widget)

        layout = QHBoxLayout()

        layout.addWidget(contacts_scroll_area, 1)
        layout.addWidget(messages_scroll_area, 2)
        layout.setSpacing(0)

        self.setLayout(layout)


        def hide_scrollbars(event):
            contacts_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            messages_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        def show_scrollbars(event):
            contacts_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            messages_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)


        contacts_scroll_area.enterEvent = show_scrollbars
        contacts_scroll_area.leaveEvent = hide_scrollbars
        messages_scroll_area.enterEvent = show_scrollbars
        messages_scroll_area.leaveEvent = hide_scrollbars

        scrollbar_style = """
        QScrollBar:vertical {
            width: 8px; 
        }
        QScrollBar::handle:vertical {
            background: #888;
            min-height: 20px;
        }
        """

        contacts_scroll_area.setStyleSheet(scrollbar_style)
        messages_scroll_area.setStyleSheet(scrollbar_style)