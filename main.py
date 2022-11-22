import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MadeCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MadeCircles()
    ex.show()
    sys.exit(app.exec())
