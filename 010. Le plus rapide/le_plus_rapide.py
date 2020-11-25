import sys
import math

#Instanciation des variables
n = int(input())
best_t_seconds = 0
best_t = ""

for i in range(n):
    t = input()
    
    #On va convertir les temps en secondes
    t_seconds = t.split(":")
    t_seconds = int(t_seconds[0])*3600 + int(t_seconds[1])*60 + int(t_seconds[2])
    
    if i == 0 or t_seconds < best_t_seconds:
        best_t_seconds = t_seconds
        best_t = t

#Affichage du meilleur temps
print(best_t)