#APP4WE Python Coding
#Pre-natal choices
#from https://www.researchprotocols.org/2019/10/e13321/pdf accessed September 16th, 2020 
import numpy as np
import pandas as pd 
  
import numpy as np
import pandas as pd 

def ahp(m,subList):
    A = np.ones([m,m])
    k=0
            
    for l in range(0,m):
        A[l,l]=1
        for h in range(0,m):
            if l<h:
               
                A[l,h] = float(subList[k])
                A[h,l] = 1/float(subList[k]) #this part here for priority  
                k+=1

    #Computing the priority vector 
    eig_val = np.linalg.eig(A)[0].max()
    eig_vec = np.linalg.eig(A)[1][:,0]
    p = eig_vec/eig_vec.sum()
    
    #computing consistency ratio
    m=len(A)                                    # Gets the number of indicators
    n=len(A[0])
    RI=[0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51]
    R= np.linalg.matrix_rank(A)                                # For judgment rank of matrix
    V,D=np.linalg.eig(A)                                              # For judgment eigenvalues ​​and eigenvectors,VEigenvalues,DFeature vector; 
    list1 = list(V)
    B= np.max(list1)                                                      # Largest eigenvalues
    index = list1.index(B)
    C = D[:, index]                                                       # Eigenvector corresponding to #
    CI=(B-n)/(n-1)                                                          # Calculate the consistency check indicatorCI
    CR=CI/RI[n]
    
    #to signify which column we're in
    
    
    print('Priority vertex (weights of criterias) from criteria 1 to '+ str(m)+' :' )
    print(p)
    print('Consistency Ratio ' + str(CR))
    if CR > 0.1:
        print('Bad consistency Ratio\n')
    else:
        print('\n')
    return p
        
# read an excel file and convert  
# into a dataframe object
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
            m=7
            k=0
            
                
            print("preprocessed answers: "+ str(subList))
            while k<len(subList):
                if subList[k] == 9999:
                    subList[k]=1
                k+=1
            try:
                print("processed answers: "+ str(subList))
                ahp(m,subList)
                
                
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
            
            m=7
            k=0
            
                
            print("preprocessed answers: "+ str(subList))
            while k<len(subList):
                if subList[k] == 9999:
                    subList[k]=1
                k+=1
            try:
                print("processed answers: "+ str(subList))
                ahp(m,subList)
                
            except IndexError:
                print("missing values for this participant\n")
                continue
        
        
    
    
    



    

calc("APP4WE -Montréal-Phase1_2020 10 26.xlsx",'APP4WE - Questionnaires')
calc("APP4WE-Québec-Phase1_2020 10 26.xlsx",'APP4WE-Questionnaire')





