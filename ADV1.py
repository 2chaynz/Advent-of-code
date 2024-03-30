import pandas as pd 
import os 

#print(os.getcwd()) # Il faut respécifier le chemin du mac 

r = pd.read_csv('/Users/hobby/Desktop/advent of code copie/code.csv')

#print(r)
#display(r.head())
#print([i for i in r['gtlbhbjgkrb5sixfivefivetwosix'] ]) 

def sumADV():
    list = ['0','1','2','3','4','5','6','7','8','9']
    S = 0
    for i in r['gtlbhbjgkrb5sixfivefivetwosix']:
        for j in range(len(i)):
            if i[j] not in list:  
                None
            else:
                l=0
                c=-1
                while i[l] not in list:
                    l+=1
                while i[c] not in list:
                    c-=1
                S+=int( str(i[l])+str(i[c]) )
                break # pour passer au mot suivant 
    S+=55
    return S
   

print(sumADV())