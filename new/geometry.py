from math import sin, cos


def rotate_point(p, al):
    x, y = p
    return x * cos(al) - y * sin(al), x * sin(al) + y * cos(al)


def translation(p, p_n):
    return p[0] + p_n[0], p[1] + p_n[1]
