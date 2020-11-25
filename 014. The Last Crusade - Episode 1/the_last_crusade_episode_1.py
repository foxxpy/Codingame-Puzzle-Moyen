import sys
import math

def get_type_room(position, table):
    return table[position[1]][position[0]]

w, h = [int(i) for i in input().split()]

#Dictionnaire associant les entrées d'une pièce avec leur sortie
type_rooms = {
    "1" : {"LEFT" : "BOTTOM", "TOP" : "BOTTOM", "RIGHT" : "BOTTOM"},
    "2" : {"LEFT" : "RIGHT", "RIGHT" : "LEFT"},
    "3" : {"TOP" : "BOTTOM"},
    "4" : {"TOP" : "LEFT", "RIGHT" : "BOTTOM"},
    "5" : {"TOP" : "RIGHT", "LEFT" : "BOTTOM"},
    "6" : {"LEFT" : "RIGHT", "RIGHT" : "LEFT"},
    "7" : {"TOP" : "BOTTOM", "RIGHT" : "BOTTOM"},
    "8" : {"LEFT" : "BOTTOM", "RIGHT" : "BOTTOM"},
    "9" : {"LEFT" : "BOTTOM", "TOP" : "BOTTOM"},
    "10" : {"TOP" : "LEFT"},
    "11" : {"TOP" : "RIGHT"},
    "12" : {"RIGHT" : "BOTTOM"},
    "13" : {"LEFT" : "BOTTOM"}
}

#Associe la sortie d'une pièce avec la modification des coordonnées qu'elle engendre
direction_to_coordinates = {
    "BOTTOM" : (0,1),
    "LEFT" : (-1, 0),
    "RIGHT" : (1,0)
}

labyrinth = list()

#On ajoute les lignes à notre labyrinthe
for i in range(h):
    line = input().split(" ")  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    labyrinth.append(line)

ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    xi, yi, pos = input().split()
    position_indy = (int(xi), int(yi))
    print(xi, yi, pos, file=sys.stderr)

    #On récupère le type de pièce dans laquelle est Indy, on regarde quelle sortie est associée à l'entrée par laquelle arrive Indy
    #On modifie la position d'indy
    type_room = get_type_room(position_indy, labyrinth)
    exit = type_rooms[str(type_room)][pos]
    position_indy = tuple(map(sum, zip(position_indy, direction_to_coordinates[exit])))


    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(str(position_indy[0])+" "+str(position_indy[1]))