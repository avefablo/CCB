

ans = sympy.solve_poly_system([symx + symy - inv1,
                               symx * symy - inv2,
                               symx * symy * symz - inv3],
                              symx, symy, symz)

i = 0 if ans[0][1] < 0 else 1
A1 = ans[i][0]
C1 = ans[i][1]
F1 = ans[i][2]

a_can = sqrt(F1/A1)
b_can = sqrt(F1/C1)
c_can = sqrt(a*a+b*b)
focus1 = (-c_can, 0)
focus2 = (c_can, 0)


# перенос
alpha = atan(2 * B / (A - C)) / 2
ans3, = sympy.solve_poly_system([A * symx + B * symy + D,
                                 D * symx + C * symy + E],
                                symx, symy)



