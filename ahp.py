#APP4WE Python Coding
#Pre-natal choices
#from https://www.researchprotocols.org/2019/10/e13321/pdf accessed September 16th, 2020 
import numpy as np
import pandas as pd 
  
# read an excel file and convert  
# into a dataframe object 
df = pd.DataFrame(pd.read_excel("dummydata.xlsx")) 
del df['Questions']  
# show the dataframe 
#print(df) 
columns = list(df)


n= 6 #6 criterias


A = np.ones([n,n])
for m in columns:#just to compute all the columns automatically otherwise would have to manually change names of columns
    
    l=list(df[m])
    if len(l)>15: #because we are only concerning ourselves with the first 6 criterias, as the 7th one is optional
        del l[:-1]
    #print(l)
    k=0
    for i in range(0,n):
        A[i,i]=1
        for j in range(0,n):
            
            if i<j:
               
                A[i,j] = float(l[k])
                A[j,i] = 1/float(l[k]) #this part here for priority  
                k+=1

    #Computing the priority vector 
    eig_val = np.linalg.eig(A)[0].max()
    eig_vec = np.linalg.eig(A)[1][:,0]
    p = eig_vec/eig_vec.sum()
    
    #computing consistency ratio
    V,D=np.linalg.eig(A)
    list1 = list(V)
    B= np.max(list1)
    index = list1.index(eig_val)
    CI = D[:, index]                                                        #Eigenvector corresponding to #
    CR=(B-n)/(n-1)
    print(m)#to signify which column we're in
    print('ahp matrix')
    print(A)
    print('Priority vertex (weights of criterias) from criteria 1 to 6:')
    print(p)
    print('Consistency Ratio')
    if CR>0.1:
        
        print(str(CR)+' Good Consistency Ratio')
    else:
        print(str(CR)+' Bad Consistency Ratio-value error somewhere in column ' + str(m))





