import sys
import math

length_all_path = dict()
max_length = 2

def go_to_next_person(influencers, influence):
    global length_all_path
    global max_length

    if not influencers in length_all_path.keys():
        length_all_path[influencers] = 1
    else:
        return

    if influencers not in influence.keys():
        return

    for next_person in influence[influencers]:
        go_to_next_person(next_person, influence)
        if length_all_path[influencers] < 1 + length_all_path[next_person]:
            length_all_path[influencers] = 1 + length_all_path[next_person]
        if length_all_path[influencers] > max_length:
            max_length = length_all_path[influencers]

    return

#Instanciation des variables
n = int(input())  # the number of relationships of influence
influence = dict()
start = []
list_y = []

#On récupère les points
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]

    #On ajoute les relations dans le dictionnaire influence
    if x in influence.keys():
        influence[x].append(y)
    else:
        influence[x] = [y]

    #On stocke l'individualité de chaque personne et on cherche les points de départ
    #Sachant qu'un y est quelqu'un d'influencé, il ne peut être un point de départ
    #Donc on garde en mémoire les personnes influencées
    if not x in start and not x in list_y:
        start.append(x)

    if x in start and x in list_y:
        start.remove(x)

    if y in start:
        start.remove(y)

    if not y in list_y:
        list_y.append(y)

#On teste tous les points de départs, donc les numéros des personnes qui ne sont pas influencées
for influencers in start:
    go_to_next_person(influencers, influence)


print(max_length)