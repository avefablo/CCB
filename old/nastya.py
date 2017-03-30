import matplotlib.pyplot as plt
import sympy, math, numpy
from sympy.abc import x as symx, y as symy, z as symz


def f(x):
    return a * x + b + c / (x + d)


def lineBrez(x0, y0, R):
    x = 0
    y = -R
    Delta = 2 * (1 - R)
    while x + y <= 0:
        plt.scatter(x, y, s=1)
        plt.scatter(-x, y, s=1)
        plt.scatter(x, -y, s=1)
        plt.scatter(-x, -y, s=1)
        plt.scatter(-y, -x, s=1)
        plt.scatter(-y, x, s=1)
        plt.scatter(y, -x, s=1)
        plt.scatter(y, x, s=1)
        print((x, y))
        if (Delta < 0):
            if (2 * (Delta - y) > 1):
                y += 1
                Delta += 2 * y + 1
            x += 1
            Delta += 2 * x + 1
        else:
            if (2 * (Delta - x) < 1):
                x += 1
                Delta += 2 * x + 1
            y += 1
            Delta += 2 * y + 1


def distPoints(x1, y1, x2, y2):
    print((x1, y1, x2, y2), ((x1 - x2) ** 2 + (y1 - y2) ** 2))
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def delta(a, b, x, y):
    return abs(-b * b * x * x + a * a * y * y - a * a * b * b)


def reX(x, x0, y, y0, al):
    return x * math.cos(al) + y * math.sin(al) + x0


def reY(x, x0, y, y0, al):
    return -x * math.sin(al) + y * math.cos(al) + y0


def findFocus():
    A, B, C, D, E, F = (a, -1 / 2, 0, (b + a * d) / 2, -d / 2, b * d + c)
    print((A, B, C, D, E, F))
    g = numpy.linalg.det([[A, B, D],
                          [B, C, E],
                          [D, E, F]])
    h = numpy.linalg.det([[A, B], [B, C]])
    s = A + C
    k = g / h * (-1)
    print(g, h, s)
    # print(sympy.solve_poly_system([symx + symy-50, symx*symy-400, symx*symy*symz+16000], symx, symy, symz))
    # mB = (s+math.sqrt(s*s - 4*h))/2
    # nA = h / mB
    # nA *= k #это а
    # mB *= k #б
    all = sympy.solve_poly_system([symx + symy - s, symx * symy - h, symx * symy * symz - g], symx, symy, symz)
    nA = all[0][0]
    mB = all[0][1]
    k = all[0][2]
    if mB > 0:
        nA = all[1][0]
        mB = -all[1][1]
        k = all[1][2]
    print(nA, mB, k)
    nA = math.sqrt(k / nA)
    mB = math.sqrt(k / mB)
    cF = math.sqrt(mB * mB + nA * nA)
    # угол
    al = - math.atan(2 * B / (A - C)) / 2
    x0y0 = sympy.solve_poly_system([A * symx + B * symy + D, B * symx + C * symy + E], symx, symy)
    print(x0y0)
    x0 = -x0y0[0][0]
    y0 = -x0y0[0][1]
    fX1 = reX(cF, x0, 0, y0, al)
    fY1 = reY(cF, x0, 0, y0, al)
    fX2 = reX(-cF, x0, 0, y0, al)
    fY2 = reY(-cF, x0, 0, y0, al)

    # xCyC = sympy.solve_poly_system([(symx - fX1) / (fX2-fX1) - (symy - fY1) / (fY2 - fY1), math.sqrt((symx - fX1)**2 + (symy - fY1)**2) - math.sqrt((symx - fX2)**2) + (symy - fY2)**2 - 2*nA], symx, symy)
    # xCyC = sympy.solve_poly_system([(symx - fX1) / (fX2-fX1) - (symy - fY1) / (fY2 - fY1), a*symx + +b+c/(symx + d) - symy], symx, symy)
    xK = sympy.Symbol('x')
    Q = (fY2 - fY1) / (fX2 - fX1)
    xxx = sympy.solvers.solve(
        a * xK ** 2 + xK * (a * d + d - (fY2 - fY1) / (fX2 - fX1) + fX1 - d) + b * d + c + (fY2 - fY1) * d * fX1 / (
        fX2 - fX1), xK)
    antosha = sympy.solvers.solve(Q * (xK - fX1) * (xK + d) + fY1 * (xK + d) - a * xK * (xK + d) - b * (xK + d) - c, xK)
    print(xxx)
    print(antosha)
    # print(xCyC)

    #   print(al)
    # nFx1 = cF*math.cos(al)
    # nFy1 = cF*math.sin(al)
    # nFx2 = -cF*math.cos(al)
    # nFy2 = -cF*math.sin(al)
    x = 2
    y = 0
    plt.scatter(x, y, s=1)
    # while x< 200:
    #    pass


a = 1
b = 1
c = 3
d = 1
cF = 0
findFocus()
# lineBrez(0,10,10)
plt.xlim(-100, 800)
plt.ylim(-100, 800)
plt.show()
plt.close()
