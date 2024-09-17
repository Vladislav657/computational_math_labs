def iterate(res):
    new = []
    for i in range(len(res)):
        x_i = 0
        for j in range(len(new_system[i + 1]) - 1):
            x_i += new_system[i + 1][j] * res[j]
        x_i += new_system[i + 1][-1]
        new.append(x_i)
    return new


def accurate(res_0, res_1):
    for i in range(len(res_0)):
        if abs(abs(res_0[i]) - abs(res_1[i])) >= 1e-6:
            return False
    return True


m = []
r = []
with open("lineq", 'r', encoding="utf-8") as f:
    n = int(f.readline())
    for i in range(n):
        line = list(map(float, f.readline().strip().split()))
        m.append([])
        for j in range(n):
            m[i].append(line[j])
        r.append(line[-1])


new_system = {}
r_0 = []
for i in range(len(m)):
    max_j = 0
    for j in range(1, len(m)):
        if m[i][j] > m[i][max_j]:
            max_j = j
    if max_j + 1 in new_system.keys():
        print("итерационный процесс не сходится")
        exit(0)
    new_system[max_j + 1] = []
    for j in range(len(m)):
        if j == max_j:
            new_system[max_j + 1].append(0)
            continue
        new_system[max_j + 1].append(-m[i][j] / m[i][max_j])
    new_system[max_j + 1].append(r[i] / m[i][max_j])
    r_0.append(r[i] / m[i][max_j])


r_1 = iterate(r_0)
while not accurate(r_0, r_1):
    r_0, r_1 = r_1.copy(), iterate(r_1)

print("me :)")
for i in range(len(r)):
    print(f"x{i + 1} = {r_1[i]};")


from scipy import linalg
import numpy as np

A = np.array(m)
B = np.array(r).reshape(len(r), 1)

X = linalg.solve(A, B)

print("\nNumpy + Scipy :")
for i in range(len(r)):
    print(f"x{i + 1} = {X[i][0]};")
