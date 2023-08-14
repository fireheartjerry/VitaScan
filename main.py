from classes.MainWindow import MainWindow
from PySide6.QtWidgets import QApplication
from sys import argv

if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow(app)
    window.show()

    app.exec()