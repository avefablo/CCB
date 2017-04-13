import math, tkinter, numpy, sympy
# from win32api import GetSystemMetrics
from sympy.abc import x as symx, y as symy, z as symz


def f(x):
    return a * x + b + c / (x + d)


def delta(a, f1, f2, p):
    return abs(abs(dist(f1, p) - dist(f2, p)) - 2*a)


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def draw(st, points, a, verbose=False):
    x = st[0]
    y = st[1]
    canv.create_oval(x-1+xMax/2, yMax-1- (y+yMax/2), x+xMax/2, yMax-(y+yMax/2), fill='red', outline='red')
    canv.pack()
    while abs(x) < xMax / 2 and abs(y) < yMax / 2:
        minDist = float('inf')
        if verbose:
            print("Current point: {} {}".format(x, y))
        for l in points:
            tempDist = delta(a, (fX1, fY1), (fX2, fY2), l(x, y))
            if tempDist < minDist:
                minCoord = l(x, y)
                minDist = tempDist
            if verbose:
                print("\tNew point: {} {}. Dist: {}".format(*l(x, y), tempDist))

        x = minCoord[0]
        y = minCoord[1]
        canv.create_oval(x+xMax/2, yMax-(y+yMax/2),
                         x+xMax/2, yMax-(y+yMax/2), fill='red', outline='red')
        canv.pack()


def rotatePoint(f, al, x0, y0):
    return (f * math.cos(al) + x0, f * math.sin(al) + y0)


def checkAngle(p1, p2):
    eps = 0.001
    print ((abs(f(p1[0]) - p1[1]), abs(f(p2[0]) - p2[1])))
    return abs(f(p1[0]) - p1[1]) < eps and abs(f(p2[0]) - p2[1]) < eps


def ivalStarts(A, B, C, D, E, cF, al, aX):
    x0y0 = sympy.solve_poly_system([A*symx + B*symy + D, B*symx + C*symy + E], symx, symy)
    x0 = x0y0[0][0]
    y0 = x0y0[0][1]
    global fX1, fY1, fX2, fY2
    fX1, fY1 = rotatePoint(cF, al, x0, y0)
    fX2, fY2 = rotatePoint(-cF, al, x0, y0)
    return (rotatePoint(aX, al, x0, y0), rotatePoint(-aX, al, x0, y0))


def findStart(A, B, C, D, E, cF, al, aX):
    starts = ivalStarts(A, B, C, D, E, cF, al, aX)
    if not checkAngle(starts[0], starts[1]):
        al -= 1.57
        starts = ivalStarts(A, B, C, D, E, cF, al, aX)
    if not checkAngle(starts[0], starts[1]):
        al += 2*1.57
        starts = ivalStarts(A, B, C, D, E, cF, al, aX)
    printGip(starts, al, aX)


def printGip(starts, al, aX):
    x1, y1 = starts[0][0], starts[0][1]
    x2, y2 = starts[1][0], starts[1][1]
    points = detectPoints(al)
    print(al)
    left = points[0]
    right = points[1]
    for x in left:
        print(x(0, 0))

    draw((x1, y1), left, aX)
    draw((x1, y1), right, aX, True)
    draw((x2, y2), left, aX)
    draw((x2, y2), right, aX)


def detectPoints(al):
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
        if f0(0,0)[0]*math.tan(al) - f0(0,0)[1] >= 0:
            left.append(f0)
        if f0(0,0)[0]*math.tan(al) - f0(0,0)[1] <= 0:
            right.append(f0)
    return (left, right)


def findCoefficients():
    A, B, C, D, E, F = (a, -1/2, 0, (b+a*d)/2, -d/2, b*d+c)
    #A, B, C, D, E, F = [-3, -1 / 2, 0, -4 / 2, 5 / 2, -1]
    print((A, B, C, D, E, F))
    g = numpy.linalg.det([[ A, B, D],
                    [B, C, E],
                    [D, E, F]])
    h = numpy.linalg.det([[A, B], [B, C]])
    s = A + C
    all = sympy.solve_poly_system([symx + symy-s, symx*symy-h, symx*symy*symz-g], symx, symy, symz)
    k = -all[0][2]
    nA = all[0][0] / k
    mB = all[0][1] / k
    if nA < 0:
        nA = all[1][0] / k
        mB = all[1][1] / k
    if mB<0:
        mB *= -1
    nA2 = 1 / nA #a^2
    mB2 = 1 / mB #b^2

    cF = math.sqrt(mB2 + nA2) #x f
    aX = math.sqrt(nA2)
    al = math.atan(2*B / (A-C) )/2 #true
    findStart(A, B, C, D, E, cF, al, aX)

win = tkinter.Tk()
# xMax = GetSystemMetrics(0)
xMax = 800
# yMax = GetSystemMetrics(1)
yMax = 600

canv = tkinter.Canvas(win, height=yMax-30, width=xMax-10)
canv.create_line(xMax/2, 0, xMax/2, yMax)
canv.create_line(0,yMax/2, xMax, yMax/2)
a, b, c, d = (-1, 65, -2733, 42)
a, b, c,d = (1,1,1,1)
#a, b, c,d = (1,100,1,1)

findCoefficients()
win.mainloop()