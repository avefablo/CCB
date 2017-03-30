from math import sin, cos


def rotate_point(p, al):
    x, y = p
    return x * cos(al) + y * sin(al), -x * sin(al) + y * cos(al)


def translation(x0, y0, x, y):
    return x + x0, y + y0
