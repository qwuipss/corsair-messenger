from json import loads
from .Client import Client
from PyQt6.QtCore import pyqtSignal, QThread

class MessageReceiveThread(QThread):

    message_received = pyqtSignal(dict)

    websocket_connection_error_detected = pyqtSignal(Exception)

    def __init__(self, client: Client) -> None:
        
        super().__init__()

        self.__client = client

    def run(self) -> None:
        
        while True:
            
            try:
                message = self.__client.receive_message()
                self.message_received.emit(loads(message))
            except Exception as exc:
                self.websocket_connection_error_detected.emit(exc)
                