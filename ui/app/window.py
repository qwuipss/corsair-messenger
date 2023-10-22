from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from .gui.PushButton import PushButton

WINDOW_TITLE = "corsair"

#self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        
        super().__init__()

        self.setWindowTitle(WINDOW_TITLE)

        central_widget = QWidget(self)

        grid_layout = QVBoxLayout()

        grid_layout.setSpacing(20)

        grid_layout.addWidget(QLabel("CORSAIR"), alignment=Qt.AlignmentFlag.AlignCenter)

        grid_layout.addWidget(QLabel("Login"), alignment=Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(QLineEdit(), alignment=Qt.AlignmentFlag.AlignCenter)

        password_label = QLabel("Password")
        grid_layout.addWidget(password_label, alignment=Qt.AlignmentFlag.AlignCenter)

        password_line_edit = QLineEdit()
        password_line_edit.setFixedWidth(320)
        password_line_edit.setStyleSheet("""
                                         border: 1px solid black; 
                                         border-bottom-left-radius: 10px;
                                         border-bottom-right-radius: 10px;
                                         border-top-left-radius: 10px;
                                         border-top-right-radius: 10px;
                                         width: 100px;
                                         """)

        password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        grid_layout.addWidget(password_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        enter_button = QPushButton("Enter")
        grid_layout.addWidget(enter_button, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(grid_layout)

        self.setMinimumWidth(500)
        self.setFixedHeight(grid_layout.sizeHint().height())


        self.setCentralWidget(central_widget)

