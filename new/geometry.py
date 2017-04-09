from math import sin, cos, sqrt


def rotate_point(p, al):
    x, y = p
    return x * cos(al) - y * sin(al), x * sin(al) + y * cos(al)


def translation(p, p_n):
    return p[0] + p_n[0], p[1] + p_n[1]


def dist(p1, p2):
    return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)


def get_int_point(p):
    return round(p[0]), round(p[1])

def get_line_coeffs(p1, p2):
    return p1[1]-p2[1], p2[0]-p1[0], p1[0]*p2[1] - p2[0]*p1[1]


def full_translation(p, np, al):
    return translation(rotate_point(p, al), np)


def get_left_right_points(line):
    f1 = lambda x, y: (x - 1, y + 1)
    f2 = lambda x, y: (x, y + 1)
    f3 = lambda x, y: (x + 1, y + 1)
    f4 = lambda x, y: (x - 1, y)
    f5 = lambda x, y: (x + 1, y)
    f6 = lambda x, y: (x - 1, y - 1)
    f7 = lambda x, y: (x, y - 1)
    f8 = lambda x, y: (x + 1, y - 1)
    transform = [f1, f2, f3, f4, f5, f6, f7, f8]
    right = []
    left = []
    for f in transform:
        p = f(0, 0)
        if line[0] * p[0] + line[1] * p[1] + line[2] > 0:
            right.append(f)
        elif line[0] * p[0] + line[1] * p[1] + line[2] < 0:
            left.append(f)
        else:
            left.append(f)
            right.append(f)
    return left, right
