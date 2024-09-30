import numpy as np
from matplotlib.pyplot import figure


W11 = np.array([[1, 1, -1.5], [1, 1, -0.5], [1, 1, -1]])
W12 = np.array([1, 1, -1])

XX1 = [np.array([np.random.sample(), np.random.sample(), 1]).T for _ in range(100)]

W21 = np.array([[1, 1, -1.5], [-1, -1, 0.5], [-1, 1, -0.5], [1, -1, -0.5]])
W22 = np.array([1, 1, 1, 1])

XX2 = [np.array([np.random.sample(), np.random.sample(), 1]).T for _ in range(100)]


def forwardNN1(x):
    z1 = W11.dot(x)
    y1 = np.heaviside(z1, 0)
    z2 = W12.dot(y1)
    y2 = np.heaviside(z2, 0)
    return y2


def forwardNN2(x):
    z1 = W21.dot(x)
    y1 = np.heaviside(z1, 0)
    z2 = W22.dot(y1)
    y2 = np.heaviside(z2, 0)
    return y2


fig1 = figure()
ax1 = fig1.add_subplot(111)
ax1.grid()
c, d = None, None
for X in XX1:
    if forwardNN1(X):
        c = ax1.scatter(X[0], X[1], color='green')
    else:
        d = ax1.scatter(X[0], X[1], color='red')
ax1.plot([0.5, 1], [1, 0.5], color='blue')
ax1.plot([0, 0.5], [0.5, 0], color='blue')
ax1.plot([0, 1], [1, 0], color='blue')
ax1.legend((c, d), ['кошка', 'собака'])
fig1.show()


fig2 = figure()
ax2 = fig2.add_subplot(111)
ax2.grid()
c, d = None, None
for X in XX2:
    if forwardNN2(X):
        c = ax2.scatter(X[0], X[1], color='green')
    else:
        d = ax2.scatter(X[0], X[1], color='red')
ax2.plot([0, 0.5], [0.5, 1], color='blue')
ax2.plot([0.5, 1], [1, 0.5], color='blue')
ax2.plot([0.5, 1], [0, 0.5], color='blue')
ax2.plot([0, 0.5], [0.5, 0], color='blue')
ax2.legend((c, d), ['кошка', 'собака'])
fig2.show()
