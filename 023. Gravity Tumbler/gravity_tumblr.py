import sys
import math

def turn_raster(list_raster, width, height, count_odd):

    new_list_raster = list()
    #On applique la gravité aux briques en les amenant sur la gauche
    for raster in list_raster:
        num_brick = raster.count("#")
        raster = "#"*num_brick + "."*(len(raster)-num_brick)
        new_list_raster.append(raster)

    #Si on a un nombre impair, c'est qu'on tourne la grille de 90 dégrés
    if count_odd:
        list_raster = list()
        #On tourne le raster
        for i in range(width):
            column = ""
            for line in new_list_raster:
                column += line[len(line)-i-1]
            list_raster.append(column)

            width, height = height, width

    #Sinon on tourne la grille de 180 degrés
    else:
        list_raster = new_list_raster

    return list_raster, width, height

#Instanciation des variables
width, height = [int(i) for i in input().split()]
count = int(input())
count_odd = True if count % 2 == 1 else False
list_raster = list()

#On récupère les lignes
for i in range(height):
    raster = input()
    list_raster.append(raster)

list_raster, width, height = turn_raster(list_raster, width, height, count_odd)

for raster in list_raster:
    if count_odd:
        print(raster)
    else:
        print(raster[::-1])
