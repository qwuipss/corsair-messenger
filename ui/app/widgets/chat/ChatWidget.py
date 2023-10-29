#from .ChatWidgetQSS import ChatWidgetQSS
from PyQt6 import QtGui
from PyQt6 import QtCore
from PyQt6.QtCore import (
    Qt, QSize, 
)
from PyQt6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem, 
    QScrollArea, QGridLayout, QMessageBox, QFrame, QSizePolicy, QAbstractScrollArea,
)

class ChatWidget(QWidget):

    def __init__(self, parent: QWidget, font_id: int) -> None:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        if not isinstance(font_id, int):
            raise TypeError(type(font_id))
        
        super().__init__()

        (contacts_scroll_area, contacts_layout) = ChatWidget.__get_scroll_area_and_layout(parent)
        (messages_scroll_area, messages_layout) = ChatWidget.__get_scroll_area_and_layout(parent)

        for i in range(500):
            contacts_layout.addWidget(QLabel(f"contact{i}"))
        for i in range(550):
            al = QLabel()
            al.setText("mes")
            messages_layout.addWidget(al)
            al.setAlignment(Qt.AlignmentFlag.AlignRight)

        contacts_extended_layout = QVBoxLayout()
        contacts_extended_layout.setContentsMargins(0,0,0,0)
        contacts_extended_layout.addWidget(QLineEdit())
        contacts_extended_layout.addWidget(contacts_scroll_area)

        messages_extended_layout = QVBoxLayout()
        current_contact = QLabel("Anonymous")
        messages_extended_layout.addWidget(current_contact)
        messages_extended_layout.addWidget(messages_scroll_area)
        messages_extended_layout.addWidget(QLineEdit())

        layout = QHBoxLayout()
        layout.addLayout(contacts_extended_layout, 2)
        # layout.addWidget(contacts_scroll_area, 2)
        layout.addLayout(messages_extended_layout, 5)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)

    @staticmethod
    def __get_scroll_area_and_layout(parent: QWidget) -> tuple[QScrollArea, QVBoxLayout]:

        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        layout = QVBoxLayout()

        widget = QWidget()

        widget.setLayout(layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_area.setWidget(widget)

        scroll_area.enterEvent = \
            lambda _: scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        scroll_area.leaveEvent = \
            lambda _: scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scrollbar_style = """
            QScrollBar:vertical {
                width: 3px;
                background: #555555;
            }
            QScrollBar::sub-page:vertical, QScrollBar::add-page:vertical{
                background: #0c0c0c;
            }
            QScrollBar::handle:vertical {
                min-height: 0px;
                background: #555555;
            }   
            """
        
        scroll_area.setStyleSheet(scrollbar_style)
        #scroll_area.setFixedHeight(parent.size().height())
        #scroll_area.setFrameShape(QFrame.Shape(0))

        return (scroll_area, layout)
