import sys
import math

#Instanciation des variables
n = int(input())
b = input()
d_min = -1
furthest_index = 0
furthest_index_answer = 0
occupied_urinals = list()

#On récupère la liste des index des urinoires occupés
for i in range(n):
    if b[i] == "!":
        occupied_urinals.append(i)
        
#On calcule la distance entre chaque urinoire
for i in range(len(occupied_urinals)):
    
    if i == 0:
        distance = occupied_urinals[i]
        furthest_index = 0
        
    elif i < len(occupied_urinals):
        debut = occupied_urinals[i-1]
        fin = occupied_urinals[i]
        furthest_index = int((debut+fin) / 2) if (fin - debut - 1) % 2 == 1 else int(math.floor((debut+fin)/2))
        distance = furthest_index - debut
        
    if i == len(occupied_urinals) - 1 and (n-occupied_urinals[i]-1) > occupied_urinals[i]:
        distance = n - occupied_urinals[i]-1
        furthest_index = n - 1
        
    if distance > d_min:
        d_min = distance
        furthest_index_answer = furthest_index

#Affichage de la réponse
print(furthest_index_answer)
