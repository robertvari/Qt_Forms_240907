from PySide6.QtWidgets import QWidget, QApplication
import sys

# Subclass QWidget to define our own window
class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration Form")
        self.showMaximized(True)
