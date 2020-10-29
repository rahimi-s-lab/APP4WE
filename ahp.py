#APP4WE Python Coding
#Pre-natal choices
#from https://www.researchprotocols.org/2019/10/e13321/pdf accessed September 16th, 2020 
import numpy as np
import pandas as pd 
  
# read an excel file and convert  
# into a dataframe object 
df = pd.DataFrame(pd.read_excel("dummydata.xlsx")) 
  
# show the dataframe 
#print(df) 


# Number of options: taken from:resprot_v8i10e13321_app2.pdf ; accessed September 16th, 2020 
n = 4
b=1
# Creating default matrix of ones
A = np.ones([n,n])
# Running a for loop to take answer from user and populate the upper triangular elements
for i in range(0,n):
    for j in range(0,n):
        if i<j:
             aij = float(df.P1[j]) #this to change for later
             #because depends on nature of raw data
             A[i,j] = float(aij) #Upper triangular elements
             A[j,i] = 1/float(aij) #Lower triangular elements


#compute the priority vector by normalizing the eigen vector of the largest eigen value.
#he elements in this eigen vector are the weights of the criteria.
eig_val = np.linalg.eig(A)[0].max()
e = np.linalg.eig(A)[1][:,0]
p = e/e.sum()
 #just to see the criterias against each other
print(A)

#this is to combine the above together such that it is more cohesive together-more reliable
#also starting here, this is for the 4 different 
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
                aij = float(df.P1[j]) 
                A[i,j] = float(aij)
                A[j,i] = 1/float(aij) #this part here for priority
                
    #Computing the priority vector (basically the weight)-for basically each category 
    eig_val = np.linalg.eig(A)[0].max()
    eig_vec = np.linalg.eig(A)[1][:,0]
    n=len(A[0])
    p = eig_vec/eig_vec.sum()
    V,D=np.linalg.eig(A)                                              # For judgment eigenvalues ​​and eigenvectors,VEigenvalues,DFeature vector; 
    list1 = list(V)
    #B= np.max(list1)        #something wrong here....                                              # Largest eigenvalues
    index = list1.index(B)
    C = D[:, index]                                                        #Eigenvector corresponding to #
    CI=(B-n)/(n-1)
    #print(CI)
    return p, eig_val, CI

#labeling the different criterias, where it measures out importance of {SIPS,IPS, NIPT, and no test} which is the alternative set
#just to be able to access more easily
print("\n")
pr_c = pairwise_matrix(4)[0]  #All Criteria
print("\n")
pr_c0 = pairwise_matrix(4)[0] #Criteria 0: Waiting time
print("\n")
pr_c1 = pairwise_matrix(4)[0] #Criteria 1: Cost
print("\n")
pr_c2 = pairwise_matrix(4)[0] #Criteria 2: Detection rate
print("\n")
pr_c3 = pairwise_matrix(4)[0] #Criteria 3: Week of pregnancy that test will be taken
print("\n")
# final step is to get the weighted arithmetic sum to yield the rank vector
r = pr_c0*pr_c[0] + pr_c1*pr_c[1] + pr_c2*pr_c[2]+pr_c3*pr_c[3]
print(r)
print(pairwise_matrix(4))


