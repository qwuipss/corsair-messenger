from .MessageEdit import MessageEdit
from .Scrollarea import Scrollarea
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QTextEdit, QLabel, QMainWindow

class MessagesWidget(QWidget):

    def __init__(self, main_window: QMainWindow, parent: QWidget) -> None:

        if not isinstance(main_window, QMainWindow):
            raise TypeError(type(main_window))
        
        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        super().__init__(parent)

        self.__current_contact_name = QLabel("clynqz")
        self.__messages_scrollarea = Scrollarea(main_window, self.__messages_scrollarea_enter_event, self.__messages_scrollarea_leave_event)
        self.__message_edit = self.__get_message_edit(main_window, parent)

        self.messages_scrollarea.verticalScrollBar().hide()

        self.__current_contact_name.setObjectName("currentContactName")
        self.__messages_scrollarea.verticalScrollBar().setObjectName("messagesScrollbar")

    @property
    def current_contact_name(self) -> QLabel:
        return self.__current_contact_name
    
    @property
    def messages_scrollarea(self) -> Scrollarea:
        return self.__messages_scrollarea
    
    @property
    def message_edit(self) -> QTextEdit:
        return self.__message_edit

    def add_message(self, message: QWidget) -> None:

        if not isinstance(message, QWidget):
            raise TypeError(type(message)) 

        self.__messages_scrollarea.add_widget(message)

    def __get_message_edit(self, main_window: QMainWindow, parent: QWidget) -> QTextEdit:

        if not isinstance(main_window, QMainWindow):
            raise TypeError(type(main_window))
        
        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))
        
        message_edit_max_height = main_window.size().height() // 3
        
        message_edit = MessageEdit(parent, message_edit_max_height)

        message_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        message_edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        message_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        message_edit.setObjectName("messageEdit")

        return message_edit
    
    def __messages_scrollarea_enter_event(self) -> None:

        self.__messages_scrollarea.verticalScrollBar().show()

    def __messages_scrollarea_leave_event(self) -> None:

        self.__messages_scrollarea.verticalScrollBar().hide()
