import sys
import os
from app.MainWindow import MainWindow
from SharedConstants import SECOND_WINDOW
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":

    app = QApplication(sys.argv)

    main_window = MainWindow()

    main_window.show()
    
    if SECOND_WINDOW:

        second_window = MainWindow()
    
        second_window.show()

    app.exec()

    os._exit(1)
