from new.qtcarcas import Carcass, Drawer
from PyQt4 import QtGui, QtCore
import operator

class HyperbolaDrawer(Drawer):
    def __init__(self, c):
        super().__init__()
        self.size = None
        self.curve = c

    def draw(self, qp):
        qp.setPen(QtCore.Qt.blue)
        for x in self.curve.starting_points:
            self.draw_point(x, qp)
        qp.setPen(QtCore.Qt.black)
        self.brez_process(self.curve.starting_points[0], self.curve.left_points, qp)
        self.brez_process(self.curve.starting_points[1], self.curve.left_points, qp)
        self.brez_process(self.curve.starting_points[0], self.curve.right_points, qp)
        self.brez_process(self.curve.starting_points[1], self.curve.right_points, qp)

    def brez_process(self, point, directs, qp):
        x, y = point
        while abs(x) <= self.size.width()/2 and abs(y) <= self.size.height()/2:
            deltas = [self.curve.get_distance_from_foci(p(x, y)) for p in directs]
            min_index, min_value = min(enumerate(deltas), key=operator.itemgetter(1))
            x, y = directs[min_index](x, y)
            self.draw_point((x, y), qp)

    def draw_point(self, p, qp):
        qp.drawPoint(p[0] + self.size.width()/2, self.size.height() - (p[1] + self.size.height()/2))
