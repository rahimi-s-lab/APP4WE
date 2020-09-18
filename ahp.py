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
eig_val = np.linalg.eig(A)[0].max()
e = np.linalg.eig(A)[1][:,0]
p = e/e.sum()


def pairwise_matrix(n):
    """
    #call this function for generating pair-wise comparison matrices
    #and priority vectors for assessing
    #each of the alternative against each criterion
    >>> pairwise_matrix(4)
    How important is option0 over option1 ?: How important is option0 over option2 ?: How important is option0 over option3 ?: How important is option1 over option2 ?: How important is option1 over option3 ?: How important is option2 over option3 ?: (array([0.32999777+0.j, 0.32999777+0.j, 0.19958055+0.j, 0.14042392+0.j]), (4.0606470275541415+0j))
    
    """
    A = np.ones([n,n])
    
    for i in range(0,n):
        for j in range(0,n):
            if i<j:
                aij = input('How important is option{} over option{} ?: '.format(i,j)) #to channge according to format of raw data
                A[i,j] = float(aij)
                A[j,i] = 1/float(aij)
    #Computing the priority vector 
    eig_val = np.linalg.eig(A)[0].max()
    eig_vec = np.linalg.eig(A)[1][:,0]
    p = eig_vec/eig_vec.sum()
    return p, eig_val





if __name__ == "__main__":
    import doctest
    doctest.testmod()
