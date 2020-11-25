import sys
import math

#Instanciation des variables
n = int(input())
max = 0
max_loss = 0

for i in input().split():
    v = int(i)
    
    #On regarde si on tombe sur une nouvelle valeur maximale
    max = v if v > max else max
    
    #Si la différence entre v et la valeur maximale retenue est supérieure à max_loss
    if max - v > max_loss:
        max_loss = max - v


print(-max_loss)