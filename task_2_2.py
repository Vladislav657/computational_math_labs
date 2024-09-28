from linalgfuncs import get_matrix, det, reduce_matrix


def iterate(matrix, res):
    new = []
    for i in range(len(res)):
        x_i = 0
        for j in range(len(matrix[i]) - 1):
            x_i += matrix[i][j] * res[j]
        x_i += matrix[i][-1]
        new.append(x_i)
    return new


def accurate(res_0, res_1):
    for i in range(len(res_0)):
        if abs(abs(res_0[i]) - abs(res_1[i])) >= 1e-6:
            return False
    return True


m, r = get_matrix()
if det(m) == 0:
    print("Уравнения линейно зависимы")
    exit(0)
m, r = reduce_matrix(m, r)

m_0 = []
r_0 = []
for i in range(len(m)):
    m_0.append([])
    for j in range(len(m)):
        if i == j:
            continue
        m_0[i].append(-m[i][j] / m[i][i])
    m_0[i].append(r[i] / m[i][i])
    r_0.append(1)


r_1 = iterate(m_0, r_0)
while not accurate(r_0, r_1):
    r_0, r_1 = r_1.copy(), iterate(m_0, r_1)

print("me :)")
for i in range(len(r)):
    print(f"x{i + 1} = {r_1[i]};")


from numpy import linalg, array

A = array(m)
B = array(r).reshape(len(r), 1)

X = linalg.solve(A, B)

print("\nNumpy + Scipy :")
for i in range(len(r)):
    print(f"x{i + 1} = {X[i][0]};")
