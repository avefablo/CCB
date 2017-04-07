from curve import Curve
from PyQt4 import QtGui
import sys
from new.drawer import HyperbolaDrawer
from new.qtcarcas import Carcass

"""
#print('enter a b c d: ', end='')
#a, b, c, d = [int(x) for x in input().split(' ')]
#A, B, C, D, E, F = [a, -1 / 2, 0, b / 2, -d / 2, c]

# Ax^2 + 2Bxy + Cy^2 + 2Dx + 2Ey + F = 0

a = 1
b = 1
c = -1
d = 0
A, B, C, D, E, F = (a, -1 / 2, 0, (b + a * d) / 2, -d / 2, b * d + c)  # true
x = Curve(A, B, C, D, E, F)

# Drawer.draw(c)
"""

def main():
    c0 = Curve(7, 8, -2, -7, 8, -2180)  # методичка
    app = QtGui.QApplication(sys.argv)
    ex = Carcass(HyperbolaDrawer(c0))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
