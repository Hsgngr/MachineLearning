"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 23:41 27.02.2020
"""
import numpy as np
import math

learning_rate = 0.2
# Input
X = [0., 1.]
# Target
y = [1., 0.]

# Initial Weights
# v=[[-1,0],[0,1]]
# w=[[1,-1],[0,1]]
v = np.array([[-1., 0.], [0., 1.]])
w = np.array([[1., -1.], [0., 1.]])

bias = 1


# Sigmoid function for activation function:
def g(x):
    # return 1 / (1 + math.exp(-x))
    return x


def mlp(X, y, v, w, iter_count):
    result = np.zeros_like(y)

    for p in range(iter_count):
        u = np.array([[0., 0.], [0., 0.]])

        for i in range(X.__len__()):
            for j in range(len(v[0])):
                u[i][j] = (X[i] * v[i][j])
        # Decreasin the dimesions of the matrix from 2x2 to 1x2 by summing the rows in a single row.
        u = u.sum(axis=0)
        # Add biases
        for i in range(u.size):
            u[i] = u[i] + bias
        # Activation Function
        z = u.copy()
        for i in range(u.size):
            z[i] = g(u[i])

        # Second Layer of MLP
        a = np.array([[0., 0.], [0., 0.]])

        for i in range(z.__len__()):
            for j in range(len(w[0])):
                a[i][j] = (z[i] * w[i][j])

        # Decreasin the dimesions of the matrix from 2x2 to 1x2 by summing the rows in a single row.
        a = a.sum(axis=0)

        # Add biases
        for i in range(a.size):
            a[i] = a[i] + 1

        # Activation Function
        yNew = a.copy()
        for i in range(a.size):
            yNew[i] = g(a[i])

        print(yNew)

        # BackPass
        Delta = np.zeros((1, y.__len__()), dtype=float)
        for s in range(Delta.shape[1]):
            Delta[0][s] = -(y[s] - yNew[s])

        # I need to take only first element of Delta thats why I'm doing this. It ia an issue in numpy.
        # Delta = [1, 2]
        Delta = Delta[0]

        Delta2 = np.zeros(w.shape, dtype=float)

        for i in range(len(Delta)):
            for j in range(len(w[0])):
                Delta2[i][j] = (Delta[i] * w[j][i])

        Delta2 = Delta2.sum(axis=0)

        # Recalculating Weights:
        X = np.asarray(X)

        for i in range(v.shape[0]):
            for j in range(v.shape[1]):
                # print('v{x}{y}: {val}'.format(x=i+1,y=j+1, val= tempv[i][j]), end= '')

                v[i][j] = v[i][j] - (learning_rate * Delta2[i] * X[j])

                # print('| v{x}{y}: {val}'.format(x=i+1,y=j+1, val= tempv[i][j]))

        for i in range(w.shape[0]):
            for j in range(w.shape[1]):
                # print('w{x}{y}: {val}'.format(x=i+1,y=j+1, val= tempw[i][j]), end= '')

                w[i][j] = w[i][j] - (learning_rate * Delta[i] * z[j])

                # print('| w{x}{y}: {val}'.format(x=i+1,y=j+1, val= tempw[i][j]))
    result = yNew
    return result


# Input
X = [0., 1.]
# Target
y = [1., 0.]

ans = mlp(X, y, v, w, 1000)
print('Answer is {t} {j}'.format(t=ans[0], j=ans[1]))
# print(v)
# print(w)
