import numpy
import sympy
from sympy.abc import x as symx, y as symy, z as symz
from math import atan, sqrt, pi, sin, cos, tan
import new.geometry as geom


class Curve:
    def __init__(self, A, B, C, D, E, F):
        self.A, self.B, self.C, self.D, self.E, self.F = A, B, C, D, E, F
        # угол
        rotate_angle = pi / 4
        if A != C:  # я проверка угла
            rotate_angle = atan(2 * B / (A - C)) / 2
        # начало ск
        new_point = sympy.solve_poly_system([A * symx + B * symy + D,
                                             B * symx + C * symy + E],
                                            symx, symy)[0]
        # нахождение коэффициентов
        inv1 = self.A + self.C
        inv2 = numpy.linalg.det([[self.A, self.B], [self.B, self.C]])
        inv3 = numpy.linalg.det([[self.A, self.B, self.D],
                                 [self.B, self.C, self.E],
                                 [self.D, self.E, self.F]])
        ans = sympy.solve_poly_system([symx + symy - inv1,
                                       symx * symy - inv2,
                                       symx * symy * symz - inv3],
                                      symx, symy, symz)
        coeffs = list(filter(lambda x: x[1] * x[2] >= 0, ans))
        if coeffs is None:
            raise HyperbolaException("not a hyp")
        coeffs = coeffs[0]
        if coeffs[0] < 0 and coeffs[1] > 0 and coeffs[2] > 0:
            coeffs = [-x for x in coeffs]
        A1 = coeffs[0]
        C1 = coeffs[1]
        F1 = -coeffs[2]
        a_can_big = F1 / A1
        b_can_big = F1 / -C1
        a_can = sqrt(a_can_big)
        b_can = sqrt(b_can_big)
        c_can = sqrt(a_can_big + b_can_big)
        self.delta = 2 * a_can
        self.starting_points = [(geom.full_translation(x, new_point, rotate_angle))
                                for x in [(-a_can, 0), (a_can, 0)]]
        self.focuses = [geom.full_translation(x, new_point, rotate_angle)
                        for x in [(-c_can, 0), (c_can, 0)]]
        line = (tan(rotate_angle), -1, 0)

        if not self.self_check():
            self.starting_points = [geom.rotate_point(x, -pi / 2)
                                    for x in self.starting_points]
            self.focuses = [geom.rotate_point(x, -pi / 2)
                            for x in self.focuses]
            line = (tan(rotate_angle - pi / 2), -1, 0)
        if not self.self_check():
            raise HyperbolaException("wrong starting points")
        self.left_points, self.right_points = geom.get_left_right_points(line)

    def insert_point_into_curve(self, p):
        x, y = p
        A, B, C, D, E, F = self.A, self.B, self.C, self.D, self.E, self.F
        return A * x * x + 2 * B * x * y + C * y * y + 2 * D * x + 2 * E * y + F
        # Ax^2 + 2Bxy + Cy^2 + 2Dx + 2Ey + F = 0

    def self_check(self):
        for x in self.starting_points:
            t = abs(self.insert_point_into_curve(x))
            ch1 = abs(self.insert_point_into_curve(x)) < 1e-8
            ch2 = self.get_distance_from_focuses(x) < 1e-8
            return ch1 and ch2

    def get_distance_from_focuses(self, p):
        return abs(abs(geom.dist(p, self.focuses[0]) - geom.dist(p, self.focuses[1])) - self.delta)


class HyperbolaException(Exception):
    pass
