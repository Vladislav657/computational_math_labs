def det(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    res = 0
    for i in range(len(matrix)):
        submatrix = []
        for j in range(1, len(matrix)):
            submatrix.append([])
            for k in range(len(matrix)):
                if k != i:
                    submatrix[j - 1].append(matrix[j][k])
        res += matrix[0][i] * det(submatrix) * (-1) ** i
    return res

m = []
r = []
with open("lineq", 'r', encoding="utf-8") as f:
    n = int(f.readline())
    for i in range(n):
        line = list(map(int, f.readline().strip().split()))
        m.append([])
        for j in range(n):
            m[i].append(line[j])
        r.append(line[-1])

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


from scipy import linalg
import numpy as np

A = np.array(m)
B = np.array(r).reshape(len(r), 1)

X = linalg.solve(A, B)

print("\nNumpy + Scipy :")
for i in range(len(r)):
    print(f"x{i + 1} = {X[i][0]};")
