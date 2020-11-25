import sys
import math

#Instanciation des variables
n = int(input())
stones = []

#On ajoute nos pierres à notre liste de pierres
for i in input().split():
    level = int(i)
    stones.append(level)
    
permutation = True

#Tant qu'on a trouvé des pierres à fusionner, on continue
while (permutation):
    i = 0
    permutation = False
    stones_temp = []
    stones = sorted(stones)
    
    #On parcourt la liste de pierres pour trouver les pierres qui peuvent fusionner entre elles
    while(i < len(stones)):

        if i+1 < len(stones) and stones[i] == stones[i+1]:
            stones_temp.append(stones[i]+1)
            stones.pop(i+1)
            stones.pop(i)
            permutation = True
            
        else:
            i = i + 1
            
        stones = stones_temp+stones[:]
        stones_temp = []
    
#Affichage du résultat
print(len(stones))