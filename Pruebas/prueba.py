from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top= 150
        self.left= 150
        self.width = 500
        self.height = 500
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def paintEvent(self, event):
        painter = QPainter(self)
        path = QPainterPath()
        points = [
            QPoint(20,40),
            QPoint(60,10),
            QPoint(100,50),
            QPoint(80,200),
            QPoint(200,300),
            QPoint(150,400),
            QPoint(350,450),
            QPoint(400,350),
            QPoint(34,350),
            ]

        # draw small red dots on each point
        painter.setPen(QtCore.Qt.red)
        painter.setBrush(QBrush(Qt.red))
        for i in range(len(points)):
            painter.drawEllipse(points[i], 3, 3)

        painter.setPen(QtCore.Qt.blue)
        painter.setBrush(QBrush(Qt.red, Qt.NoBrush)) #reset the brush
        path.moveTo(points[0])

        # connect the points with blue straight lines
        #for i in range(len(points)-1):  # 1 less than length
        #    path.lineTo(points[i+1])

        # connect points with curve
        for i in range(0,len(points),2):
            path.quadTo(points[i], points[i+1])

        painter.drawPath(path)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())