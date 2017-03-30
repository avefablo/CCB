import numpy
import sympy
from sympy.abc import x as symx, y as symy, z as symz
from math import atan, sqrt, pi


class Curve:
    def __init__(self, A, B, C, D, E, F):
        self.A, self.B, self.C, self.D, self.E, self.F = A, B, C, D, E, F
        self.inv1 = self.A + self.C
        self.inv2 = numpy.linalg.det([[self.A, self.B], [self.B, self.C]])
        self.inv3 = numpy.linalg.det([[self.A, self.B, self.D],
                                      [self.B, self.C, self.E],
                                      [self.D, self.E, self.F]])
        if A - C == 0: # я проверка угла
            self.rotate_angle = pi / 4
        else:
            self.rotate_angle = atan(2 * B / (A - C)) / 2
        self.new_point, = sympy.solve_poly_system([A * symx + B * symy + D,
                                                   B * symx + C * symy + E],
                                                  symx, symy)
        ans = sympy.solve_poly_system([symx + symy - self.inv1,
                                       symx * symy - self.inv2,
                                       symx * symy * symz - self.inv3],
                                      symx, symy, symz)
        #меня надо поправить!
        A1 = ans[1][0]
        C1 = ans[1][1]
        F1 = -ans[1][2]

        a_can = sqrt(F1 / A1)
        b_can = sqrt(F1 / -C1)
        c_can = sqrt(a_can * a_can + b_can * b_can)
        print() # я для дебага
