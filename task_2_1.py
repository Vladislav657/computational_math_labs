from linalgfuncs import det, get_matrix

m, r = get_matrix()

d = det(m)
if d == 0:
    print("Уравнения линейно зависимы")
    exit(0)

print("me :)")
for i in range(len(r)):
    m_i = [row.copy() for row in m]
    for j in range(len(r)):
        m_i[j][i] = r[j]
    print(f"x{i + 1} = {det(m_i) / d};")


from numpy import linalg, array

A = array(m)
B = array(r).reshape(len(r), 1)

X = linalg.solve(A, B)

print("\nNumpy :")
for i in range(len(r)):
    print(f"x{i + 1} = {X[i][0]};")
