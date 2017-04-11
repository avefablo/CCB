from curve import Curve
from PyQt4 import QtGui
import sys
from drawer import HyperbolaDrawer
from qtcarcas import Carcass


def main():
    a, b, c, d = [float(x) for x in input('Enter a b c d: ').strip().split(' ')]
    # A, B, C, D, E, F = [a, -1 / 2, 0, b / 2, -d / 2, c]
    A, B, C, D, E, F = [1, -0.5, 0, 1.0, -0.5, 2]
    x = Curve(A, B, C, D, E, F)

    x = Curve(3, -0.5, 0, 6.5, -0.5, 9)  # методичка
    app = QtGui.QApplication(sys.argv)
    ex = Carcass(HyperbolaDrawer(x))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
