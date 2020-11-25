import sys
import math

def check_node(to_the_right, x, y, width, height):
    """On teste si il existe un noeud à droite ou en bas"""
    axe = x if to_the_right else y
    length = width if to_the_right else height

    i=1 #On cherche sur un axe si il existe un noeud
    while(axe+i < length):
        node = list_line[y][x+i] if to_the_right else list_line[y+i][x]
        if node == "0" and to_the_right: #Si il existe un noeud sur la droite
            return str(x+i)+" "+str(y)+" "
        elif node == "0" and not to_the_right: #Si il existe un noeud en dessous
            return str(x)+" "+str(y+i)
        i = i + 1
                
    return str(-1)+" "+str(-1)+" "

#Instanciation des variables
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
list_line = list()

#On récupère chaque ligne contenant les noeuds
for i in range(height):
    line = input()
    list_line.append(line)

#On parcourt tous les noeuds pour afficher les informations demandées dans l'énoncé
for y in range(height):
    for x in range(width):
        node_information = ""
        
        #Si on est sur un noeud, on recherche si il a un noeud à sa droite et en-dessous
        if list_line[y][x] == "0":
            node_information += str(x)+" "+str(y)+" "

            node_information += check_node(True, x, y, width, height)
            node_information += check_node(False, x, y, width, height)

            print(node_information)
