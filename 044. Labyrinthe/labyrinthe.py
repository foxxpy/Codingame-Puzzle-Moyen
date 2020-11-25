import sys
import math

def move(x, y, h, w):
    global labyrinth
    global already_visited

    exit_position = []

    #On teste si on est sur une sortie : un point en bordure du labyrinthe
    if (x==0 or y==0 or x==w-1 or y==w-1) and labyrinth[y][x] == ".":
        exit_position.append((x,y))

    #On ajoute cette case aux cases déjà visitées
    already_visited.append((x,y))

    #Si on peut aller à gauche
    if x > 0 and labyrinth[y][x-1] != "#" and not (x-1, y) in already_visited:
        exit_position += move(x-1, y, h, w)

    #Si on peut aller à droite
    if x < w-1 and labyrinth[y][x+1] != "#" and not (x+1, y) in already_visited:
        exit_position += move(x+1, y, h, w)

    #Si on peut aller en haut
    if y > 0 and labyrinth[y-1][x] != "#" and not (x, y-1) in already_visited:
        exit_position += move(x, y-1, h, w)

    #Si on peut aller en bas
    if y < h-1 and labyrinth[y+1][x] != "#" and not (x, y+1) in already_visited:
        exit_position += move(x, y+1, h, w)

    return exit_position

    
#Instanciation des variables
w, h = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]
labyrinth = []
already_visited = list()
exit_lab = []

#On ajoute les lignes du labyrinthe à notre labyrinthe
for i in range(h):
    r = list(input())
    labyrinth.append(r)

exit_lab = move(x, y, h, w)
exit_lab = sorted(exit_lab, key=lambda x: (x[0], x[1]))

print(len(exit_lab))
for ex in exit_lab:
    print(ex[0], ex[1])
