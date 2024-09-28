from numpy import sqrt, arange
import matplotlib.pyplot as plt


N = 5

dates = ['07.02.2024',
         '06.02.2024',
         '09.02.2024',
         '10.03.2024',
         '06.12.2023']

hydra = [720.2,
         730.0,
         740.0,
         750.0,
         760.0]

barometer = [sum([721.55, 721.78, 722.02, 722.49, 723]) / 5,
             sum([732.71, 732.9, 733.0, 733.1, 733.13]) / 5,
             sum([741.34, 741.89, 742.0, 742.49, 742.9]) / 5,
             sum([749.44, 750.0, 750.55, 751.0, 752.1]) / 5,
             sum([758.07, 759.01, 760.0, 760.54, 761.0]) / 5]

sum_x = sum(hydra)
sum_y = sum(barometer)
sum_x2 = sum(list(map(lambda x: x ** 2, hydra)))
sum_xy = sum([hydra[i] * barometer[i] for i in range(N)])


def df_da0(x, y):
    return 2 * (N * x + sum_x * y - sum_y)


def df_da1(x, y):
    return 2 * (sum_x * x + sum_x2 * y - sum_xy)


a0 = a1 = 5
lmd = 1e-8
epsilon = 1e-8
step_a0 = lmd * df_da0(a0, a1)
step_a1 = lmd * df_da1(a0, a1)
while sqrt((a0 - step_a0 - a0) ** 2 + (a1 - step_a1 - a1) ** 2) >= epsilon:
    a0, a1 = a0 - step_a0, a1 - step_a1
    step_a0 = lmd * df_da0(a0, a1)
    step_a1 = lmd * df_da1(a0, a1)

X = arange(710, 770, 5)
plt.grid()
plt.xlabel('Hydra')
plt.ylabel('Barometer')
plt.scatter(hydra, barometer, color='green')
plt.plot(X, [a0 + a1 * x0 for x0 in X], color='blue')
plt.show()
