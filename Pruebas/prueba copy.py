import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainterPath, QPainter


class MouseTracker(QWidget):
    distance_from_target = 0
    mouse_x_pos = 0
    mouse_y_pos = 0
    target_x_pos = 500
    target_y_pos = 250
    vel = 60  # pixels per second

    def __init__(self, parent=None):
        super(MouseTracker, self).__init__(parent=parent)
        self.initUI()
        self.setMouseTracking(True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.changePosition)
        self.timer.start(1000 / self.vel)

    def changePosition(self):
        

        self.update()

    def initUI(self):
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('Mouse Tracker')
        self.label = QLabel(self)
        self.label.resize(500, 40)
        self.show()

    def mouseMoveEvent(self, event):
        self.mouse_x_pos = event.x()
        self.mouse_y_pos = event.y()
        print(event.x(),event.y())
        self.update()

    def mousePressEvent(self, event):
        self.target_x_pos = event.x()
        self.target_y_pos = event.y()
        print(event.x(),event.y())
        self.update()

    def paintEvent(self, event):
        q = QPainterPath()
        
        q.moveTo(100,100)
        #q.lineTo(200, 200)
        q.cubicTo(0, 0, 0, 0, 0, 0)
        painter = QPainter(self)
        painter.drawPath(q)
        #q.begin(self)
        #q.drawLine(self.mouse_x_pos, self.mouse_y_pos, self.target_x_pos, self.target_y_pos)


app = QApplication(sys.argv)
w = MouseTracker()
sys.exit(app.exec_())