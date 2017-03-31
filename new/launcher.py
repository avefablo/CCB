from curve import Curve


#print('enter a b c d: ', end='')
#a, b, c, d = [int(x) for x in input().split(' ')]
#A, B, C, D, E, F = [a, -1 / 2, 0, b / 2, -d / 2, c]

# Ax^2 + 2Bxy + Cy^2 + 2Dx + 2Ey + F = 0
c = Curve(0, 2, 3, 8, 6, -36)

# c = Curve(A, B, C, D, E, F)

# Drawer.draw(c)
