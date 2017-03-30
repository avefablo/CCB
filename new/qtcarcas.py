import sys, random
from PyQt4 import QtGui, QtCore


class Carcass(QtGui.QWidget):
    def __init__(self, drawer):
        super(Carcass, self).__init__()
        self.drawer = drawer
        self.drawer.size = self.size()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(50, 50, 480, 480)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        self.drawer.size = self.size()
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawer.draw(qp)
        qp.end()


class Drawer:
    def __init__(self):
        pass

    def draw(self, qp):
        pass
