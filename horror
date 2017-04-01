import matplotlib.pyplot as plt
import sympy, math, numpy, tkinter
from win32api import GetSystemMetrics
from sympy.abc import x as symx, y as symy, z as symz


def f(x):
    return a * x + b + c / (x + d)


def distPoints(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)    
    
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
   # print(x0y0)
    x0 = x0y0[0][0]
    y0 = x0y0[0][1]

    fX1 = cF * math.cos(al) + x0
    fY1 = cF *math.sin(al) + y0
    fX2 = -cF * math.cos(al) + x0
    fY2 = -cF *math.sin(al) + y0
    xK   = sympy.Symbol('x')
    m = fY2 - fY1
    n = fX2 - fX1
    Q0 = m/n - a
    Q1 = m * d / n - fX1 * m / n - fY1 - a*d - b
    Q2 = -fY1 * d - b*d -c
    temp = sympy.solvers.solve(Q0*xK**2 + xK * Q1 + Q2, xK)
    print (temp)
    xM1 = temp[0]
    yM1 = f(xM1)
    xM2 = temp[1]
    yM2 = f(xM2)
    x = xM1
    y = yM1

    while x < xMax/2 and y< yMax/2:
        v1 = abs(abs(distPoints(fX1, fY1, x+1, y) - distPoints(fX2, fY2, x+1, y)) - delta)
        v2 = abs(abs(distPoints(fX1, fY1, x, y+1) - distPoints(fX2, fY2, x, y+1)) - delta)
        if v1 < v2:
            x += 1
        else:
            y += 1
        canv.create_oval(x-1+xMax/2, yMax- (y-1+yMax/2), x+1+xMax/2,yMax-( y+1+yMax/2))
        canv.pack()
    x = xM1
    y = yM1
    while x < xMax/2 and y > -yMax/2:
        v1 = abs(abs(distPoints(fX1, fY1, x+1, y) - distPoints(fX2, fY2, x+1, y)) - delta)
        v2 = abs(abs(distPoints(fX1, fY1, x, y-1) - distPoints(fX2, fY2, x, y-1)) - delta)
        if v1 < v2:
            x += 1
        else:
            y -= 1
        canv.create_oval(x-1+xMax/2, yMax- (y-1+yMax/2), x+1+xMax/2,yMax-( y+1+yMax/2))
        canv.pack()


win = tkinter.Tk()
xMax = GetSystemMetrics(0)
yMax = GetSystemMetrics(1)

canv = tkinter.Canvas(win, height=yMax-30, width=xMax-10)
#canv = tkinter.Canvas(win, height=10, width=10)
#plt.scatter(5 + xMax/2, 1 + yMax/2, s=5)
a = 1
b = 1
c = -1
d = 0
cF = 0
findFocus()
#plt.xlim(-xMax/2, xMax/2)
#plt.ylim(-yMax/2, yMax/2)
#plt.show()
#plt.close()
win.mainloop()
