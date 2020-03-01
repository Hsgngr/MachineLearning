"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 14:51 11.02.2020
"""
import numpy as np

# # Input
# X = [1., 2.]
# # Target
# y = [1., 0.]
# v = np.array([[1., 3., 4], [1., 2., 5.]])
# u = np.array([[0., 0., 0.], [0., 0., 0.]])
#
# for i in range(X.__len__()):
#     for j in range(len(v[0])):
#         u[i][j] = (X[i] * v[i][j])
#
# # Second Layer of MLP
# a = np.array([[0., 0.], [0., 0.]])

w = np.array([[1, -1], [0, 1]])

Delta = [1, 2]
Delta2 = np.zeros(w.shape, dtype=float)

for i in range(len(Delta)):
    for j in range(len(w[0])):
        Delta2[i][j] = (Delta[i] * w[j][i])

Delta2= Delta2.sum(axis=0)
print(Delta2)