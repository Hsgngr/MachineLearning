"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 14:27 3.03.2020
"""
import numpy as np
from numpy import linalg
from scipy.io import loadmat
from scipy.spatial.distance import cdist
from scipy.spatial import distance

matfile = loadmat('sem5_q1_centres.mat')
matfile2 = loadmat('sem5_q1_points.mat')
centres = matfile['centres']
points = matfile2['points']

distance1 = np.zeros((len(points[:]), len(centres[:])), dtype=float)

for i in range(len(points[:])):  # every row
    for j in range(len(centres[:])):
        d = distance.euclidean(centres[j], points[i])
        # print('({i} , {j})'.format(i=i,j=j))
        distance1[i][j] = d
