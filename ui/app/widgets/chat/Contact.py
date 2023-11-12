from PyQt6.QtWidgets import QLabel, QWidget

class Contact(QLabel):
    
    def __init__(self, parent: QWidget, id: int, name: str) -> None:
        
        if not isinstance(parent, QWidget):
            raise TypeError(type(parent))

        if not isinstance(id, int):
            raise TypeError(type(id))

        if not isinstance(name, str):
            raise TypeError(name)

        super().__init__(name, parent)

        self.__id = id

    @property
    def id(self) -> int:
        return self.__id