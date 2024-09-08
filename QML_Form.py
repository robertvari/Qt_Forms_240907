from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
import os, sys

APP_ROOT = os.path.dirname(__file__)

class MyForm:
    def __init__(self):
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.engine.load(os.path.join(APP_ROOT, "form.qml"))

        if not self.engine.rootObjects():
            sys.exit(-1)
        
        sys.exit(self.app.exec())

if __name__ == "__main__":
    MyForm()