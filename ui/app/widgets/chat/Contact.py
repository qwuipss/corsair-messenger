from .Scrollarea import Scrollarea
from .Message import Message
from .MessageEdit import MessageEdit
from client.Client import Client
from typing import Callable
from PyQt6 import QtCore
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QVBoxLayout, QTextEdit, QLabel, QMainWindow, QLabel

class Contact(QLabel):
    
    def __init__(
            self, 
            id: int, 
            name: str, 
            contact_selected_callback: Callable[['Contact'], None], 
            message_sent_callback: Callable[[int, str], None],
            messages_history_load_delegate: Callable[[int, int, int], tuple[bool, Message]],
            main_window: QMainWindow
            ) -> None:
        
        if not isinstance(id, int):
            raise TypeError(type(id))

        if not isinstance(name, str):
            raise TypeError(name)
        
        if not isinstance(contact_selected_callback, Callable):
            raise TypeError(contact_selected_callback)

        super().__init__(name)

        self.__first_access = True

        self.__id = id
        self.__contact_selected_callback = contact_selected_callback
        self.__messages_history_load_delegate = messages_history_load_delegate

        self.__messages_scrollarea = Scrollarea()
        self.__message_edit = self.__get_message_edit(main_window, lambda text: message_sent_callback(receiver_id=self.__id, text=text))

        self.__messages_scrollarea.layout.addStretch(1)

        self.__scrollbar_max_value_before_loading_messages_history = None
        self.__scrollbar_value_before_add_new_message = None
        self.__last_message_self_authority = None

        
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        
        self.__up = True
        self._a()

    @property
    def id(self) -> int:
        return self.__id

    @property
    def messages_scrollarea(self) -> Scrollarea:
        return self.__messages_scrollarea
    
    @property
    def message_edit(self) -> QTextEdit:
        return self.__message_edit
    
    def mousePressEvent(self, event: QMouseEvent | None) -> None:

        super().mousePressEvent(event)

        self.__contact_selected_callback(self)

        self.setObjectName("selected")
        self.setStyleSheet("")

    def add_new_message(self, message: Message, self_authority: bool) -> None:

        message_layout = self.__create_message_layout(message, self_authority)

        self.__messages_scrollarea.layout.addLayout(message_layout)

        self.__scrollbar_value_before_add_new_message = self.__messages_scrollarea.verticalScrollBar().maximum()
        self.__last_message_self_authority = self_authority

    def __add_history_message(self, message: Message, self_authority: bool) -> None:

        message_layout = self.__create_message_layout(message, self_authority)

        self.__messages_scrollarea.layout.insertLayout(1, message_layout)

        self.__scrollbar_value_before_add_new_message = self.__messages_scrollarea.verticalScrollBar().maximum()

    def __create_message_layout(self, message: Message, self_authority: bool) -> QVBoxLayout:

        if not isinstance(message, Message):
            raise TypeError(type(message)) 
        
        if not isinstance(self_authority, bool):
            raise TypeError(type(self_authority))
        
        message.wheelEvent = lambda event: self.__messages_scrollarea.wheelEvent(event)

        message_layout = QVBoxLayout()

        alignment = QtCore.Qt.AlignmentFlag.AlignRight if self_authority else QtCore.Qt.AlignmentFlag.AlignLeft

        message_layout.addWidget(message)
        message_layout.setAlignment(alignment)

        return message_layout

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
    
    def _a(self):

        messages_layout = self.__messages_scrollarea.layout
        
        if messages_layout.count() == 1:
            first_message_id = -1
        else:
            first_message_id = messages_layout.itemAt(1).layout().itemAt(0).widget().id

        self.__scrollbar_max_value_before_loading_messages_history = self.__messages_scrollarea.verticalScrollBar().maximum()

        messages = self.__messages_history_load_delegate(self.__id, first_message_id)

        for raw_message in messages:

            message_id = raw_message["message_id"]
            sender_id = raw_message["sender_id"]
            text = raw_message["text"]

            message = Message(message_id, text)

            self.__add_history_message(message, sender_id != self.__id)

        scrollbar = self.__messages_scrollarea.verticalScrollBar()
        scrollbar.rangeChanged.connect(self._u)

    def _u(self):

        scrollbar = self.__messages_scrollarea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

        if self.__up:
            self.__messages_scrollarea.verticalScrollBar().valueChanged.connect(self.__load_messages_history_if_needed)
            self.__up = False

    def _s(self): 

        scrollbar = self.__messages_scrollarea.verticalScrollBar()
        scrollbar.rangeChanged.disconnect(self._u)
        self.__messages_scrollarea.verticalScrollBar().rangeChanged.connect(self.__range_changed_handler)

    def __load_messages_history(self) -> None:

        if self.__first_access:
            self._s()

        messages_layout = self.__messages_scrollarea.layout
        
        if messages_layout.count() == 1:
            first_message_id = -1
        else:
            first_message_id = messages_layout.itemAt(1).layout().itemAt(0).widget().id

        self.__scrollbar_max_value_before_loading_messages_history = self.__messages_scrollarea.verticalScrollBar().maximum()

        messages = self.__messages_history_load_delegate(self.__id, first_message_id)

        for raw_message in messages:

            message_id = raw_message["message_id"]
            sender_id = raw_message["sender_id"]
            text = raw_message["text"]

            message = Message(message_id, text)

            self.__add_history_message(message, sender_id != self.__id)


        if self.__first_access:
            self.__first_access = False

    def __load_messages_history_if_needed(self) -> None:
        
        scrollbar = self.__messages_scrollarea.verticalScrollBar() 

        if scrollbar.value() == 0:
            self.__load_messages_history()

    def __range_changed_handler(self) -> None:

        self.__return_scrollbar_on_position_before_loading_messages()
        self.__scroll_down_on_new_message_if_needed()

    def __scroll_down_on_new_message_if_needed(self) -> None:
        
        scrollbar = self.__messages_scrollarea.verticalScrollBar()

        if self.__last_message_self_authority or self.__scrollbar_value_before_add_new_message == scrollbar.value():
            scrollbar.setValue(scrollbar.maximum())

    def __return_scrollbar_on_position_before_loading_messages(self) -> None:

        scrollbar = self.__messages_scrollarea.verticalScrollBar()
        
        if scrollbar.value() == 0:
            maximum = scrollbar.maximum()
            scrollbar.setValue(maximum - self.__scrollbar_max_value_before_loading_messages_history)
