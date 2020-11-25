import sys
import math

def draw_board(min_x, max_x, min_y, max_y):
    """On dessine la grille"""
    board = []
    for y in range(max_y, min_y-1, -1):
        row = []
        for x in range(min_x, max_x+1):
            if x == 0 and y != 0:
                row.append("|")
            elif x != 0 and y == 0:
                row.append("-")
            elif x == 0 and y == 0:
                row.append("+")
            else:
                row.append(".")
        board.append(row)
    return board

#Instanciation des variables
all_x = []
all_y = []
min_x = -1
max_x = 1
min_y = -1
max_y = +1

n = int(input())
for i in range(n):
    x, y = [int(j) for j in input().split()]
    print(x,y,file=sys.stderr)
    all_x.append(x)
    all_y.append(y)

#On cherche les minimums et maximums de chaque abscisse, si on a au moins 1 point
if len(all_x) > 0:
    min_x = min(min(all_x), 0) - 1
    min_y = min(min(all_y), 0) - 1
    max_x = max(max(all_x), 0) + 1
    max_y = max(max(all_y), 0) + 1

print("Min x : "+str(min_x), file=sys.stderr)
print("Min y : "+str(min_y), file=sys.stderr)
print("Max x : "+str(max_x), file=sys.stderr)
print("Max y : "+str(max_y), file=sys.stderr)

#On construit le graphique sans les points
board = draw_board(min_x, max_x, min_y, max_y)

#On place les points
all_point = zip(all_x, all_y)
for point in all_point:
    j = point[0] + abs(min_x)
    i = max_y - point[1]
    board[i][j] = "*"

#On affiche le graphique
for line in board:
    for col in line:
        print(col, end="")
    print()
