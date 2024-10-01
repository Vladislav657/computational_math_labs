from random import randint


def f(x):
    return x ** 6 + 2 * x ** 5 - x ** 4 + 4 * x ** 3 - 3 * x ** 2 + 90 * x - 34


def df(x):
    return 6 * x ** 5 + 10 * x ** 4 - 4 * x ** 3 + 12 * x ** 2 - 6 * x + 90


def ddf(x):
    return 30 * x ** 4 + 40 * x ** 3 - 12 * x ** 2 + 24 * x - 6


epsilon = 1e-6

# method 1
a = 0
b = 1
while df(a) * df(b) >= 0 or df(a) > 0 or a >= b:
    a = randint(-100, 100)
    b = randint(-100, 100)

x0 = (a + b) / 2
while abs(b - a) > epsilon:
    if df(x0) == 0:
        break
    if df(a) * df(x0) < 0:
        b = x0
    if df(b) * df(x0) < 0:
        a = x0
    x0 = (a + b) / 2

print("method 1 :\n")
print(f"x = {x0}")
print(f"f'(x) = {round(df(x0), 4)}\n")


#method 2
x0 = 0
while df(x0) - ddf(x0) <= 0:
    x0 = randint(-100, 100)

x1 = x0 - f(x0) / df(x0)
while abs(x1 - x0) > epsilon:
    x0 = x1
    x1 = x1 - df(x1) / ddf(x1)
print("method 2 :\n")
print(f"x = {x1}")
print(f"f'(x) = {round(df(x1), 4)}\n")
