from linalgfuncs import det, reduce_matrix, get_matrix


m, r = get_matrix()
if det(m) == 0:
    print("Уравнения линейно зависимы")
    exit(0)


m, r = reduce_matrix(m, r)

print("me :)")
for i in range(len(r)):
    print(f"x{i + 1} = {r[i] / m[i][i]};")


from numpy import linalg, array


A = array(m)
B = array(r).reshape(len(r), 1)

X = linalg.solve(A, B)

print("\nNumpy :")
for i in range(len(r)):
    print(f"x{i + 1} = {X[i][0]};")
