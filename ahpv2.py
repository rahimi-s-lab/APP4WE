
# Filename: ahpv2.py
# Description: Analytic hierarchy process method
# Authors: Papathanasiou, J. & Ploskas, N.

from numpy import *
import scipy.sparse.linalg as sc
import matplotlib.pyplot as plt
from AHP_Final_Rank_Figure import graph, plot

# normalized column sum method
def norm(x):
 """ x is the pairwise comparison matrix for the
criteria or the alternatives
"""
k = array(sum(x, 0))
z = array([[round(x[i, j] / k[j], 3)
for j in range(x.shape[1])]
           for i in range(x.shape[0])]);
return z

# geometric mean method
def geomean(x):
 """ x is the pairwise comparison matrix for the
      criteria or the alternatives
 """
z= [1] * x.shape[0]
for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i]      
return z

# AHP method: it calls the other functions
def ahp(PCM, PCcriteria, m, n, c):

 """ PCM is the pairwise comparison matrix for the
 alternatives,  PCcriteria is the pairwise comparison
 matrix for the criteria, m is the number of the
 alternatives, n is the number of the criteria, and
 c is the method to estimate a priority vector (1 for
 eigenvector, 2 for normalized column sum, and 3 for
 geometric mean)
 """
 # calculate the priority vector of criteria
 if c == 1: # eigenvector
     val, vec = sc.eigs(PCcriteria, k = 1, which = 'LM')
     eigcriteria = real(vec)
     w = eigcriteria / sum(eigcriteria)
     w = array(w).ravel()
 elif c == 2: # normalized column sum
     normPCcriteria = norm(PCcriteria)
     w = array(sum(normPCcriteria, 1) / n)
 else: # geometric mean
     GMcriteria = geomean(PCcriteria)
     w = GMcriteria / sum(GMcriteria)
# calculate the local priority vectors for the
# alternatives
S= []
for i in range(n):
     if c == 1: # eigenvector
         val, vec = sc.eigs(PCM[i * m:i * m + m, 0:m],
             k = 1, which = 'LM')
         eigalter = real(vec)
