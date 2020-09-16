#APP4WE Python Coding
#Pre-natal choices
#from https://www.researchprotocols.org/2019/10/e13321/pdf accessed September 16th, 2020 
import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer
import operator


# Number of options: taken from:resprot_v8i10e13321_app2.pdf ; accessed September 16th, 2020 
n = 4

# Creating default matrix of ones
A = np.ones([n,n])
# Running a for loop to take answer from user and populate the upper triangular elements
for i in range(0,n):
    for j in range(0,n):
         if i<j:
             aij = input('How important is option{} over option{} ?: '.format(i,j)) #this to change for later
             #because depends on nature of raw data
             A[i,j] = float(aij) #Upper triangular elements
             A[j,i] = 1/float(aij) #Lower triangular elements


#compute the priority vector by normalizing the eigen vector of the largest eigen value.
#The elements in this eigen vector are the weights of the criteria.

egvalue = np.linalg.eig(A)[1][:,0]
p = egvalue/egvalue.sum()
