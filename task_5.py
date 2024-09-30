import numpy as np
import matplotlib.pyplot as plt


W11 = np.array([[1, 1, -1.5], [1, 1, -0.5], [1, 1, -1]])
W21 = np.array([[-1, 1, -0.5], [-1, 1, 0.5], [-1, 1, 0]])
W2 = np.array([1, 1, -1])

XX = [np.array([np.random.sample(), np.random.sample(), 1]).T for _ in range(100)]


def forwardNN1(x):
    z1 = W11.dot(x)
    y1 = np.heaviside(z1, 0)
    z2 = W2.dot(y1)
    y2 = np.heaviside(z2, 0)
    return y2


def forwardNN2(x):
    z1 = W21.dot(x)
    y1 = np.heaviside(z1, 0)
    z2 = W2.dot(y1)
    y2 = np.heaviside(z2, 0)
    return y2


plt.grid()
d, c = None, None
for X in XX:
    if forwardNN1(X) == forwardNN2(X):
        d = plt.scatter(X[0], X[1], color='red')
    else:
        c = plt.scatter(X[0], X[1], color='green')
plt.plot([0, 0.5], [0.5, 1], color='blue')
plt.plot([0.5, 1], [1, 0.5], color='blue')
plt.plot([0.5, 1], [0, 0.5], color='blue')
plt.plot([0, 0.5], [0.5, 0], color='blue')
plt.plot([0, 1], [1, 0], color='blue')
plt.plot([0, 1], [0, 1], color='blue')
plt.legend((d, c), ['собака', 'кошка'])
plt.show()
