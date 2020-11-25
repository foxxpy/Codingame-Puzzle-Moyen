import sys
import math

#Instanciation des variables
n = int(input())
list_v = input().split()
list_v = [int(x) for x in list_v]
print(list_v, file=sys.stderr)
max_loss = 0

#Boucle où on parcourt les valeurs boursières
for i in range(n):
    for j in range(i+1, n):
        if list_v[j] - list_v[i] < max_loss:
            max_loss = list_v[j] - list_v[i]
        

print(max_loss)
