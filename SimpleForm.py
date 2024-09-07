from PySide6.QtWidgets import (
    QWidget, QApplication, QLabel, QLineEdit, 
    QPushButton, QHBoxLayout, QVBoxLayout
    )
import sys

# Subclass QWidget to define our own window
class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration Form")
        # self.showMaximized()

        # Create layouts for our widgets
        main_layout = QVBoxLayout(self)

        name_layout = QHBoxLayout()
        main_layout.addLayout(name_layout)

        email_layout = QHBoxLayout()
        main_layout.addLayout(email_layout)

        address_layout = QHBoxLayout()
        main_layout.addLayout(address_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyForm()
    win.show()
    app.exec()