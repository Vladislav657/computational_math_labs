def reduce_matrix(m, r):
    for i in range(len(m)):
        for rg in [range(i + 1, len(m)), range(i)]:
            for j in rg:
                divider = m[j][i] / m[i][i]
                for k in range(len(m)):
                    m[j][k] -= m[i][k] * divider
                r[j] -= r[i] * divider
    return m, r


def det(m):
    if len(m) != len(m[0]):
        raise ValueError("Matrix must be square")
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    res = 0
    for i in range(len(m)):
        submatrix = []
        for j in range(1, len(m)):
            submatrix.append([])
            for k in range(len(m)):
                if k != i:
                    submatrix[j - 1].append(m[j][k])
        res += m[0][i] * det(submatrix) * (-1) ** i
    return res


def get_matrix():
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
    return m, r

# matrix = [
#     [1, 2, 3, 4],
#     [55, 2, 4, 6],
#     [27, 9, 24, 5],
#     [-5, 6, 11, -15]
# ]
#
# result = [6, -7, 22, 10]
#
# matrix, result = reduce_matrix(matrix, result)
# [print(*row) for row in matrix]
# print(*result, sep='\n')
