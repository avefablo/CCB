import matplotlib.pyplot as plt
import sympy, math, numpy, tkinter
# from win32api import GetSystemMetrics
from sympy.abc import x as symx, y as symy, z as symz


def f(x):
    return a * x + b + c / (x + d)


def dist(a, f, p):
    return math.sqrt((f[0] - p[0]) ** 2 + (f[1] - p[1]) ** 2) - a


def detectSign(x, al):
    print((fY2 - fY1) * (point[0] - fX1) - (fX2 - fX1) * (point[1] - fY1))
    return (fY2 - fY1) * (point[0] - fX1) - (fX2 - fX1) * (point[1] - fY1)


def findFocus():
    A, B, C, D, E, F = (a, -1 / 2, 0, (b + a * d) / 2, -d / 2, b * d + c)  # true
    A, B, C, D, E, F = (7, 8, -2, -7, 8, -218)
    g = numpy.linalg.det([[A, B, D],
                          [B, C, E],
                          [D, E, F]])
    h = numpy.linalg.det([[A, B], [B, C]])
    s = A + C
    all = sympy.solve_poly_system([symx + symy - s, symx * symy - h, symx * symy * symz - g], symx, symy, symz)
    k = -all[0][2]
    nA = all[0][0] / k
    mB = -all[0][1] / k
    if nA < 0:
        nA = all[1][0] / k
        mB = -all[1][1] / k
    nA2 = 1 / nA  # a^2
    mB2 = 1 / mB  # b^2
    cF = math.sqrt(mB2 + nA2)  # x f
    al = math.atan(2 * B / (A - C)) / 2  # true
    aX = math.sqrt(nA2)
    x0y0 = sympy.solve_poly_system([A * symx + B * symy + D, B * symx + C * symy + E], symx, symy)

    x0 = x0y0[0][0]
    y0 = x0y0[0][1]

    global fX1, fY1, fX2, fY2, xM1, yM1, yM2, xM2
    fX1 = cF * math.cos(al) + x0
    fY1 = cF * math.sin(al) + y0
    fX2 = -cF * math.cos(al) + x0
    fY2 = -cF * math.sin(al) + y0
    m = fY2 - fY1
    n = fX2 - fX1

    nAx1 = aX * math.cos(al) + x0  # старт
    nAy1 = -aX * math.sin(al) + y0
    nAx2 = -aX * math.cos(al) + x0
    nAy2 = aX * math.sin(al) + y0
    x = nAx1
    y = nAy1
    print((x, y, nAx2, nAy2))
    f1 = lambda x, y: (x - 1, y + 1)
    f2 = lambda x, y: (x, y + 1)
    f3 = lambda x, y: (x + 1, y + 1)
    f4 = lambda x, y: (x - 1, y)
    f5 = lambda x, y: (x + 1, y)
    f6 = lambda x, y: (x - 1, y - 1)
    f7 = lambda x, y: (x, y - 1)
    f8 = lambda x, y: (x + 1, y - 1)
    transform = [f1, f2, f3, f4, f5, f6, f7, f8]
    left = []
    right = []
    for f0 in transform:
        if f0(x, y)[0] * al > 0:
            left.append(f0)
        else:
            right.append(f0)
    for x in left:
        print(x(0, 0))
    print('-----')
    for x in right:
        print(x(0, 0))
    x = int(nAx1)
    y = int(nAy1)
    canv.create_oval(x + xMax / 2, yMax - (y + yMax / 2), x + xMax / 2, yMax - (y + yMax / 2))
    canv.pack()
    while abs(x) < xMax / 2 and abs(y) < yMax / 2:
        minDist = float('inf')
        minCoord = (0, 0)
        for l in right:
            tempDist = dist(aX, (fX1, fY1), l(x, y))

            if tempDist < minDist:
                minCoord = l(x, y)
                minDist = tempDist
        x = minCoord[0]
        y = minCoord[1]
        canv.create_oval(x + xMax / 2, yMax - (y + yMax / 2), x + xMax / 2, yMax - (y + yMax / 2))
        canv.pack()

    x = int(nAx1)
    y = int(nAy1)
    while abs(x) < xMax / 2 and abs(y) < yMax / 2:
        minDist = float('inf')
        minCoord = (0, 0)
        for l in left:
            print(x, y)
            tempDist = dist(aX, (fX1, fY1), l(x, y))
            if tempDist < minDist:
                minCoord = l(x, y)
                minDist = tempDist
        x = minCoord[0]
        y = minCoord[1]
        canv.create_oval(x + xMax / 2, yMax - (y + yMax / 2), x + xMax / 2, yMax - (y + yMax / 2))
        canv.pack()


win = tkinter.Tk()
# xMax = GetSystemMetrics(0)/2
# yMax = GetSystemMetrics(1)/2
xMax = 800
yMax = 600
# print (((yMax-30 )/2, (xMax-10)/2))
canv = tkinter.Canvas(win, height=yMax - 30, width=xMax - 10)
a = 0.2
b = 1.5
c = 1
d = 2
cF = 0
fX1 = 0
fY1 = 0
fX2 = 0
fY2 = 0

xM1 = 0
yM1 = 0
xM2 = 0
yM2 = 0

findFocus()
# plt.xlim(-xMax/2, xMax/2)
# plt.ylim(-yMax/2, yMax/2)
# plt.show()
# plt.close()
win.mainloop()
