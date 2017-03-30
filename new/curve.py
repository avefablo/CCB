import numpy
import sympy
from sympy.abc import x as symx, y as symy, z as symz
from math import atan, sqrt, sin, cos


class Curve:
    def __init__(self, A, B, C, D, E, F):
        self.A, self.B, self.C, self.D, self.E, self.F = A, B, C, D, E, F
        self.inv1 = self.A + self.C
        self.inv2 = numpy.linalg.det([[self.A, self.B], [self.B, self.C]])
        self.inv3 = numpy.linalg.det([[self.A, self.B, self.D],
                                      [self.B, self.C, self.E],
                                      [self.D, self.E, self.F]])
        self.rotate_angle = atan(2 * B / (A - C)) / 2
        self.new_point, = sympy.solve_poly_system([A * symx + B * symy + D,
                                                   B * symx + C * symy + E],
                                                  symx, symy)
