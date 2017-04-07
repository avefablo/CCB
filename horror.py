import matplotlib.pyplot as plt
import sympy, math, numpy, tkinter
from win32api import GetSystemMetrics
from sympy.abc import x as symx, y as symy, z as symz


def f(x):
    return a * x + b + c / (x + d)


def distPoints(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def detectSign(point):
    print ((fY2 - fY1) * (point[0] - fX1) - (fX2 - fX1) *(point[1] - fY1))
    return (fY2 - fY1) * (point[0] - fX1) - (fX2 - fX1) *(point[1] - fY1)


def findFocus():
    A,B,C,D,E,F = (a, -1/2, 0, (b+a*d)/2, -d/2, b*d+c) #true
    g = numpy.linalg.det([[ A, B, D],
                    [B, C, E],
                    [D, E, F]])
    h = numpy.linalg.det([[A, B], [B, C]])
    s = A + C
    k = g / h *(-1)
    all = sympy.solve_poly_system([symx + symy-s, symx*symy-h, symx*symy*symz-g], symx, symy, symz)
    k = -all[0][2]
    nA = all[0][0] / k
    mB = -all[0][1] / k
    if nA < 0:
        nA = all[1][0] / k
        mB = -all[1][1] / k
   # print(nA, mB, k)
    nA2 = 1 / nA #a^2
    mB2 = 1 / mB #b^2
    cF = math.sqrt(mB2 + nA2) #x f
    alN = math.atan(2*B / (A-C))/2 #true
    al =  alN #90-
    delta = 2*nA
    x0y0 = sympy.solve_poly_system([A*symx + B*symy + D, B*symx + C*symy + E], symx, symy)
    #print(x0y0)
    x0 = x0y0[0][0]
    y0 = x0y0[0][1]

    global fX1, fY1, fX2, fY2, xM1, yM1, yM2, xM2
    fX1 = cF * math.cos(al) + x0
    fY1 = cF *math.sin(al) + y0
    fX2 = -cF * math.cos(al) + x0
    fY2 = -cF *math.sin(al) + y0
    xK = sympy.Symbol('x')
    m = fY2 - fY1
    n = fX2 - fX1

    Q0 = m/n - a
    Q1 = m * d / n - fX1 * m / n + fY1 - a*d - b
    Q2 = -fX1 * d *m/n - b*d -c +fY1*d
   # print (Q0, Q1, Q2)
    temp = sympy.solvers.solve(Q0*xK**2 + xK * Q1 + Q2, xK)
    print (sympy.solvers.solve((xK - fX1)*m/n + fY1 - a*xK - b - c/(xK+d), xK))
   # print (temp, '---------/')
    xM1 = temp[0]
    yM1 = f(xM1)
    xM2 = temp[1]
    yM2 = f(xM2)
    print (detectSign((xM1, yM1)), '----')
    x = xM2
    y = yM2
    f1 = lambda x, y: (x-1, y+1)
    f2 = lambda x, y: (x, y+1)
    f3 = lambda x, y: (x+1, y+1)
    f4 = lambda x, y: (x-1, y)
    f5 = lambda x, y: (x+1, y)
    f6 = lambda x, y: (x-1, y-1)
    f7 = lambda x, y: (x, y-1)
    f8 = lambda x, y: (x+1, y-1)
    transform = [f1, f2, f3, f4, f5, f6, f7, f8]
    left = []
    right = []
    for f0 in transform:
        if detectSign(f0(x, y))> 0:
            left.append(f0)
        else:
            right.append(f0)
    print (left)
    print (right)

    x = int(xM1)
    y = int(yM1)

win = tkinter.Tk()
xMax = GetSystemMetrics(0)/2
yMax = GetSystemMetrics(1)/2
#xMax = 100
#yMax = 100
print (((yMax-30 )/2, (xMax-10)/2))
canv = tkinter.Canvas(win, height=yMax-30, width=xMax-10)
a = 0.2
b = 1.5
c = 8
d = 7
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
#plt.xlim(-xMax/2, xMax/2)
#plt.ylim(-yMax/2, yMax/2)
#plt.show()
#plt.close()
win.mainloop()