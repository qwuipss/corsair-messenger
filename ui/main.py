import sys
import os
from app.MainWindow import MainWindow
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()

    os._exit(1)
