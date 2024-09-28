"""

x ^ 4 * e ^ (sin(arcctg(x ^ 3 + x ^ 2 + x + 1) ^ 3))

"""

epsilon = 1e-6
pi = 3.141592653589793
e = 2.718281828459045


def exp(x: float) -> float:
    left_part = int(x)
    right_part = x - left_part
    s_left = 1
    if left_part < 0:
        for i in range(-left_part):
            s_left /= e
    else:
        for i in range(left_part):
            s_left *= e
    s_right = 1
    current = right_part
    n = 1
    while abs(current) >= epsilon:
        s_right += current
        current *= right_part / (n + 1)
        n += 1
    return s_left * s_right


def arcctg(x: float) -> float:
    optimized_x = x
    if abs(x) > 1:
        optimized_x = 1 / optimized_x
    s = 0
    current = optimized_x
    n = 1
    while abs(current) >= epsilon:
        s += current
        current *= ((-1) * optimized_x * optimized_x * (2 * n - 1)) / (2 * n + 1)
        n += 1
    if x < -1:
        return s + pi
    elif x > 1:
        return s
    else:
        return pi / 2 - s


def sin(x: float) -> float:
    x = x % (2 * pi)
    optimized_x = x % pi
    s = 0
    current = optimized_x
    n = 0
    while abs(current) >= epsilon:
        s += current
        current *= ((-1) * optimized_x * optimized_x) / ((2 * n + 2) * (2 * n + 3))
        n += 1
    s = s if x < pi else -s
    return s


x_in = float(input("enter x to count 'x ^ 4 * e ^ (sin(arcctg(x ^ 3 + x ^ 2 + x + 1) ^ 3))': "))
print('me :)', x_in ** 4 * exp(sin(arcctg(x_in ** 3 + x_in ** 2 + x_in + 1) ** 3)))

import numpy as np
# print(arcctg(x_in), pi / 2 - np.arctan(x_in))
print('numpy :', x_in ** 4 * np.exp(np.sin((pi / 2 - np.arctan(x_in ** 3 + x_in ** 2 + x_in + 1)) ** 3)))
