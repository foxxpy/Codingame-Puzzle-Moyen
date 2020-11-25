import sys
import math

#Instanciation des variables
m = int(input())
n = int(input())
labyrinth = []

def walk(position):
    global labyrinth, m, n
    line = position[0]
    col = position[1]
    nb_path = 0

    #Si on sort du labyrinth on renvoie 0
    if line > m - 1 or col > n - 1:
        return 0

    #Si on a atteint l'arrivée on renvoie 1
    if line == m - 1 and col == n - 1:
        return 1

    #Si on tombe sur une case invalide on renvoie 0
    elif labyrinth[line][col] == "1":
        return 0

    #Sinon on teste d'aller sur la case à droite et la case en dessous
    else:
        nb_path += walk((line+1,col))
        nb_path += walk((line, col+1))

    return nb_path

#On récupère les lignes du labyrinthe
for i in range(m):
    row = input()
    labyrinth.append(row)

nb_path = walk((0,0))

print(nb_path)
