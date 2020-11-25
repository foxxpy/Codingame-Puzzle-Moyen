import sys
import math

#Instanciation des variables
r = list()
r.append(input())
l = int(input())

for i in range(l-1):
    j = 0
    r_temp = list()
    
    #On parcourt chaque nombre de r
    while(j < len(r)):
        find_occurence = True
        k = 1
        
        #Pour chaque nombre, on regarde combien de fois il se répète
        while(j+k < len(r) and find_occurence):
            if r[j] == r[j+k]:
                k += 1
            else:
                find_occurence = False
        
        #On reconstruit la suite de Conway dans r_temp          
        r_temp.append(str(k))
        r_temp.append(r[j])              
        j = j + k
    
    r = r_temp

print(" ".join(r))
