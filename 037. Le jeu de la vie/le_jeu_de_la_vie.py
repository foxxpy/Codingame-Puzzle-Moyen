import sys
import math

def check_neighbor(universe, line, col, height, width):
    neighbors = 0
    #On vérifie toutes les cases autour d'une cellule, sauf la case de la-dite cellule
    #Donc on ne vérifie pas quand i == line et j == col puisque c'est la case de la cellule
    for i in [line-1, line, line+1]:
        if 0 <= i < height:
            for j in [col-1, col, col+1]:
                if 0 <= j < width and not (i == line and j == col) and universe[i][j] == "1":
                    print(i, j, file=sys.stderr)
                    neighbors += 1

    return neighbors



def change_state(universe, height, width):
    new_universe = []
    for i in range(height):
        new_line = ""
        for j in range(width):
            neighbors = check_neighbor(universe, i, j, height, width)

            #Conditions d'évolution de la population données dans l'énoncé
            if universe[i][j] == "1" and (neighbors < 2 or neighbors > 3):
                new_line += "0"
            elif universe[i][j] == "1" and 2 <= neighbors <= 3:
                new_line += "1"
            elif universe[i][j] == "0" and neighbors == 3:
                new_line += "1"
            else:
                new_line += "0"
        new_universe.append(new_line)
    return new_universe

#Instanciation des variables
width, height = [int(i) for i in input().split()]
universe = []

#On récupère notre population de cellules
for i in range(height):
    line = input()
    print(line, file=sys.stderr)
    universe.append(line)

universe = change_state(universe, height, width)

#Affichage du nouvel universe
for line in universe:
    print(line)
