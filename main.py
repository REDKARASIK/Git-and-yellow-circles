import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class MadeCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.can_draw = False
        self.draw_button.clicked.connect(self.paint_start)

    def paint_start(self):
        self.can_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.can_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.can_draw = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(252, 226, 5))
        r = random.randint(0, 300)
        x = random.randint(0, 839)
        y = random.randint(0, 588)
        if x + r > 839:
            x -= x + r - 839
        if y + r > 588:
            y -= y + r - 588
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MadeCircles()
    ex.show()
    sys.exit(app.exec())
