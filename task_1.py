"""

x ^ 4 * e ^ (sin(ln(x ^ 3 + x ^ 2 + x + 1)) ^ 3)

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
    change = right_part / (n + 1)
    while abs(current) >= epsilon:
        s_right += current
        current *= change
        n += 1
        change = right_part / (n + 1)
    return s_left * s_right


def ln(x: float) -> float:
    if x <= 0:
        raise ValueError("logarithm argument must be positive")

    c = 0
    while x >= e:
        x /= e
        c += 1

    x = x - 1
    s = 0
    current = x
    n = 1
    change = ((-1) * x * n) / (n + 1)
    while abs(current) >= epsilon and n <= 1e3:
        s += current
        current *= change
        n += 1
        change = ((-1) * x * n) / (n + 1)
    return c + s


def sin(x: float) -> float:
    x = x % (2 * pi)
    optimized_x = x % pi
    s = 0
    current = optimized_x
    n = 0
    change = ((-1) * optimized_x * optimized_x) / ((2 * n + 2) * (2 * n + 3))

    while abs(current) >= epsilon:
        s += current
        current *= change
        n += 1
        change = ((-1) * optimized_x * optimized_x) / ((2 * n + 2) * (2 * n + 3))

    s = s if x < pi else -s
    return s


x_in = float(input("enter x to count 'x ^ 4 * e ^ (sin(ln(x ^ 3 + x ^ 2 + x + 1)) ^ 3)': "))
ln_x = ln(x_in ** 3 + x_in ** 2 + x_in + 1)
sin_x = sin(ln_x)
sin_3_x = sin_x * sin_x * sin_x

print('me :)', x_in ** 4 * exp(sin_3_x))

import numpy as np
# print(exp(x), np.exp(x))
print('numpy :', x_in ** 4 * np.exp(np.sin(np.log(x_in ** 3 + x_in ** 2 + x_in + 1)) ** 3))
