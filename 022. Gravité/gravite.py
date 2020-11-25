import sys
import math

#Instanciation des variables
width, height = [int(i) for i in input().split()]
num_brick = []

#On instancie la liste contenant le nombre de briques par colonne
num_brick = [0]*width

#On récupère le nombre de briques par colonne
for i in range(height):
    line = input()
    for j, brick in enumerate(line):
        if brick == "#":
            num_brick[j] += 1

#On reconstruit dans liste column le résultat final
list_column = list()
for j in range(width):
    list_column.append("."*(height-num_brick[j])+"#"*num_brick[j])

#On affiche le résultat final
i = 0
for j in range(height):
    for column in list_column:
        print(column[i], end="")
    i = i + 1
    print()