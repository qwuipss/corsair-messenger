from .Scrollarea import Scrollarea
from .Message import Message
from typing import Callable
from PyQt6 import QtCore
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QMouseEvent
from typing import Callable
from .MessageEdit import MessageEdit
from .Scrollarea import Scrollarea
from .Message import Message
from PyQt6 import QtCore
from PyQt6.QtWidgets import QVBoxLayout, QTextEdit, QLabel, QMainWindow

class Contact(QLabel):
    
    def __init__(
            self, 
            id: int, 
            name: str, 
            contact_selected_callback: Callable[['Contact'], None], 
            message_sent_callback: Callable[[int, str], None],
            messages_pull_request_delegate: Callable[[int, int], tuple[bool, Message]],
            main_window: QMainWindow
            ) -> None:
        
        if not isinstance(id, int):
            raise TypeError(type(id))

        if not isinstance(name, str):
            raise TypeError(name)
        
        if not isinstance(contact_selected_callback, Callable):
            raise TypeError(contact_selected_callback)

        super().__init__(name)

        # self.__last_message_id = 0
        # self.__is_requeriable = True

        self.__id = id
        self.__contact_selected_callback = contact_selected_callback
        self.__messages_pull_request_delegate = messages_pull_request_delegate

        self.__messages_scrollarea = Scrollarea()
        self.__message_edit = self.__get_message_edit(main_window, lambda text: message_sent_callback(receiver_id=self.__id, text=text))

        self.__messages_scrollarea.layout.addStretch(1)

        scrollbar =  self.__messages_scrollarea.verticalScrollBar()       
        scrollbar.rangeChanged.connect(lambda: scrollbar.setValue(scrollbar.maximum()))

        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def messages_scrollarea(self) -> Scrollarea:

        if self.__messages_scrollarea.layout.count() == 1:
            self.__load_messages()

        return self.__messages_scrollarea
    
    @property
    def message_edit(self) -> QTextEdit:
        return self.__message_edit
    
    def mousePressEvent(self, event: QMouseEvent | None) -> None:

        super().mousePressEvent(event)

        self.__contact_selected_callback(self)

        self.setObjectName("selected")
        self.setStyleSheet("")
    
    def add_message(self, message: Message, self_author: bool) -> None:

        if not isinstance(message, Message):
            raise TypeError(type(message)) 
        
        if not isinstance(self_author, bool):
            raise TypeError(type(self_author)) 

        message_layout = QVBoxLayout()

        alignment = QtCore.Qt.AlignmentFlag.AlignRight if self_author else QtCore.Qt.AlignmentFlag.AlignLeft

        message_layout.addWidget(message)
        message_layout.setAlignment(alignment)

        self.__messages_scrollarea.layout.insertLayout(0, message_layout)   

    def __get_message_edit(self, main_window: QMainWindow, message_sent_callback: Callable[[str], None]) -> QTextEdit:

        if not isinstance(main_window, QMainWindow):
            raise TypeError(type(main_window))
        
        if not isinstance(message_sent_callback, Callable):
            raise TypeError(type(message_sent_callback))

        message_edit_max_height = int(main_window.size().height() * .3)
        
        message_edit = MessageEdit(message_edit_max_height, message_sent_callback)

        message_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        message_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        message_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        return message_edit
    
    def __load_messages(self) -> None:

        messages = self.__messages_pull_request_delegate(self.__id, 0)

        for raw_message in messages:

            message = Message(raw_message["id"], raw_message["text"])

            self.add_message(message, int(raw_message["sender_id"]) != self.__id)
