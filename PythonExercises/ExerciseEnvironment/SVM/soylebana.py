"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 15:26 10.03.2020
"""
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-15, 15, 100)  # 100 linearly spaced numbers
x2 = np.linspace(-15, 15, 100)
y = -0.6 * x1 + 0.8 * x2  # computing the values of sin(x)/x
Z = y


def g(x1, x2):
    return -0.6 * x1 + 0.8 * x2


k = np.random.random((100, 3))
k = np.sort(k, 0)  # sort x values
for i in range(len(k[:])):
    k[i][2] = g(k[i][0], k[i][1])

ax = plt.axes(projection='3d')
# Data for a three-dimensional line
zline = y
xline = x1
yline = x2
ax.plot3D(xline, yline, zline, 'gray')
ax.scatter3D(0.9, 0.3, g(0.9, 0.3), 'black')
plt.show()
