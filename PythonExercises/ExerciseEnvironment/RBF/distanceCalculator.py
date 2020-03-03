"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 18:09 3.03.2020
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

distance1 = {}

for i in range(len(centres[:])):  # every row
    print(points[i])
    for k in range(len(points[:])):
        d = distance.euclidean(centres[i], points[k])
        distance1[i, k] = d

Y = cdist(points, centres, 'euclidean')
