def rotate_point(p, al):
    x, y = p
    return x*cos(al) + y*sin(al), -x*sin(al) + y*cos(al)