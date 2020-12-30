
# Description: Analytic hierarchy process method
# Authors: Papathanasiou, J. & Ploskas, N.

from numpy import *
import scipy.sparse.linalg as sc
import matplotlib.pyplot as plt
import pandas as pd

def norm(x):
    k = array(sum(x,0))
    z= array([[round(x[i,j]/k[j],3)
               for j in range(x.shape[1])]
              for i in range(x.shape[0])])
    return z

def geomean(x):
    z=[1]*x.shape[0]
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i] = z[i] *x[i][j]
        z[i] = pow(z[i],(1/x.shape[0]))
    return z


def ahp(PCcriteria,n, c):
    """
    PCcriteria is the pairwise comparison
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

    return w



def main(c,m,subList):
    """a,b,and c areflags;if a and b are set to'y'
      they do print the results, anything else does not
      print the results. If c equals 1, the eigenvector
      method is used; if c equals 2, the normalized column
      sum method is used; otherwise, the geometric mean
      method is used
    """

    # random indices for consistency checking
    RI = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41,1.45, 1.49]

    # pairwise comparison matrix of the criteria
    
    A = ones([m,m])
    k=0
            
    for l in range(0,m):
        A[l,l]=1
        for h in range(0,m):
            if l<h:
               
                A[l,h] = float(subList[k])
                A[h,l] = 1/float(subList[k]) #this part here for priority  
                k+=1
         # consistency check for pairwise comparison matrix of
         # the criteria
    lambdamax = amax(linalg.eigvals(A).real)
    CI=(lambdamax-m)/(m-1)
    CR=CI/RI[m-1]
    
    print('Priority vertex (weights of criterias) from criteria 1 to '+ str(m)+' :' )
    print(ahp(A,m, c))
    
    print("Inconsistency index of the criteria: ", CR)
    if CR>0.1:
        print("The pairwise comparison matrix of the criteria is inconsistent\n")
    else:
        print("\n")

     

def calc(excelname,excelsheet):

    xls = pd.ExcelFile(excelname) 
    # show the dataframe 
    #print(df)
    df=pd.read_excel(xls, excelsheet)
    columns = list(df)
    Blist = []

    for i in columns:
        if 'QC' not in str(i):
            columns.remove(i)

    del columns[0:31]  
    del columns[::2]
    del columns[-1]


    for i in columns:
        Blist.append(list(df[i]))



    i=0
    subList=[]
    print(excelname + "\n")
    while i<len(Blist[0]):
    
        
        print("Participant #" + str(i+1))
        if i==0:
            for j in Blist:
                subList.append(j[i])
            i+=1
            if  (subList[4]==9999 and subList[5]==9999):#if  facteur 1 or 2 is included
                m=5
                print("preprocessed answers: "+ str(subList))

                while 9999 in subList:
                    subList.remove(9999)
                try:
                    print("processed answers: "+ str(subList))
                    main(1,m,subList)
                except IndexError:
                    print("missing values for this participant\n")
                    continue
        
            elif  subList[5]==9999:#if  only facteur 1 is included
                m=6
                print("preprocessed answers: "+ str(subList))

                while 9999 in subList:
                    subList.remove(9999)
                try:
                    print("processed answers: "+ str(subList))
                    main(1,m,subList)
                except IndexError:
                
                    print("missing values for this participant\n")
                    continue
                
           
           
            else:
                m=7 #if  facteur 1 and 2 are included
                print("preprocessed answers: "+ str(subList))

                try:
                    print("processed answers: "+ str(subList))
                    main(1,m,subList)
                except IndexError:
                    print("missing values for this participant\n")
                    continue
            
            
            
          
        else:
            n=0
            for j in Blist:

                try:
                    subList[n] = (j[i])
                except IndexError:
                    subList.append(j[i])
                n+=1
            i+=1
            if  subList[4]==9999 and subList[5]==9999: #if both facteur 1 and 2 are included
                m=5
                print("preprocessed answers: "+ str(subList))

                while 9999 in subList:
                    subList.remove(9999)
                try:
                    print("processed answers: "+ str(subList))
                    main(1,m,subList)
                except IndexError:
                    print("missing values for this participant\n")
                    continue
            elif  subList[5]==9999:#if only facteur 1 is included
                m=6
                print("preprocessed answers: "+ str(subList))

                while 9999 in subList:
                    subList.remove(9999)
                try:
                    print("processed answers: "+ str(subList))
                    main(1,m,subList)
                except IndexError:
                    print("missing values for this participant\n")
                    continue
            
            else:
                m=7 #if neither facteur 1 or 2 are included
                print("preprocessed answers: "+ str(subList))

                try:
                    print("processed answers: "+ str(subList))
                    main(1,m,subList)
                except IndexError:
                    print("missing values for this participant\n")
                    continue
    
calc("APP4WE -Montréal-Phase1_2020 10 26.xlsx",'APP4WE - Questionnaires')
#calc("APP4WE-Québec-Phase1_2020 10 26.xlsx",'APP4WE-Questionnaire')
      

