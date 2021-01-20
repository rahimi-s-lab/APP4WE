#group making decision
import numpy as np
import pandas as pd 
df = pd.DataFrame(pd.read_excel("dummydataalt.xlsx")) 
del df['PCM']  
# show the dataframe 
#print(df) 
columns = list(df)


n= 6 #6 criterias
m= 4 #4 alternatives


def pairwise_matrix(n,m):
    A = np.ones([m,m])
    s=0
    for k in columns:#just to compute all the columns automatically otherwise would have to manually change names of columns

        l=list(df[k])
        print(l)
        t=0
        
    

pairwise_matrix(6,4)
