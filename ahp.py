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
#A = np.ones([n,n])
# Running a for loop to take answer from user and populate the upper triangular elements
#for i in range(0,n):
    #for j in range(0,n):
         #if i<j:
             #aij = input('How important is option{} over option{} ?: '.format(i,j)) #this to change for later
             #because depends on nature of raw data
             #A[i,j] = float(aij) #Upper triangular elements
             #A[j,i] = 1/float(aij) #Lower triangular elements


#compute the priority vector by normalizing the eigen vector of the largest eigen value.
#The elements in this eigen vector are the weights of the criteria.
#eig_val = np.linalg.eig(A)[0].max()
#e = np.linalg.eig(A)[1][:,0]
#p = e/e.sum()


#this is to combine the above together such that it is more cohesive together-more reliable
def pairwise_matrix(n):
    """
    #call this function for generating pair-wise comparison matrices
    #and priority vectors for assessing
    #each of the alternative against each criterion: SIPS, IPS, NIPT, and no test
    >>> pairwise_matrix(4)
    (array([0.32999777+0.j, 0.32999777+0.j, 0.19958055+0.j, 0.14042392+0.j]), (4.0606470275541415+0j))
    
    """
    A = np.ones([n,n])
    
    for i in range(0,n):
        for j in range(0,n):
            if i<j:
                aij = input('How important is option{} over option{} ?: '.format(i,j)) #to channge according to the approriate collection format of raw data 
                A[i,j] = float(aij)
                A[j,i] = 1/float(aij) #this part here for priority
    print(A)            
    #Computing the priority vector (basically the weight) 
    eig_val = np.linalg.eig(A)[0].max()
    eig_vec = np.linalg.eig(A)[1][:,0]
    p = eig_vec/eig_vec.sum()
    return p, eig_val

#labeling the different criterias
pr_c = pairwise_matrix(4)[0]  #All Criteria
pr_c0 = pairwise_matrix(4)[0] #Criteria 0: Waiting time
pr_c1 = pairwise_matrix(4)[0] #Criteria 1: Cost
pr_c2 = pairwise_matrix(4)[0] #Criteria 2: Detection rate
pr_c2 = pairwise_matrix(4)[0] #Criteria 3: Week of pregnancy that test will be taken

r = pr_c0*pr_c[0] + pr_c1*pr_c[1] + pr_c2*pr_c[2]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pairwise_matrix(4)
    print(r)
