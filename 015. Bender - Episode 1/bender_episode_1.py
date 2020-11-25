import sys
import math

class Bender:
    def __init__(self, position, state, direction, heading_to="S"):
        self.position = position
        self.state = state
        self.direction_priority = direction
        self.heading_to = heading_to
        self.list_direction = []
        
    def change_state(self):
        """Change l'état de Bender"""
        if self.state == "NORMAL":
            self.state = "CASSEUR"
        else:
            self.state = "NORMAL"
            
    def change_direction_priority(self):
        """Change la priorité de direction de Bender"""
        if self.direction_priority == "NORMAL":
            self.direction_priority = "REVERSED"
        else:
            self.direction_priority = "NORMAL"
            
    def find_next_cell(self, directions_to_coordinates, direction):
        """Recherche la case suivante"""
        move = directions_to_coordinates[direction]
        next_cell = tuple(map(sum, zip(bender.position, move)))
        return next_cell
            
    def find_where_to_head(self, directions_to_coordinates, direction, city):
        """Recherche où se diriger"""
        potential_next_cell = self.find_next_cell(directions_to_coordinates, direction)
        x, y = potential_next_cell[0], potential_next_cell[1]

        if (city[y][x] in ["#", "X"] and self.state == "NORMAL") or (city[y][x] == "#" and self.state == "CASSEUR"):
            return None
        else:
            return potential_next_cell
        
directions = {
    "NORMAL" : ["S", "E", "N", "W"],
    "REVERSED" : ["W", "N", "E", "S"]
}

directions_to_coordinates = {
    "S" : (0, 1),
    "E" : (1, 0),
    "N" : (0, -1),
    "W" : (-1, 0)
}

direction_to_words = {
    "S" : "SOUTH",
    "N" : "NORTH",
    "E" : "EAST",
    "W" : "WEST"
}

#Instanciation des variables
l, c = [int(i) for i in input().split()]
city = list()
bender = None
loop = False
suicide_cabin_found = False
suicide_cabin_position = None
position_teleporteurs = []
cell_already_visited = []
nb_cell_already_visited = 0

#On récupère chaque ligne constituant la ville, et la position de départ de Bender
for i in range(l):
    row = input()
    print(row, file=sys.stderr)
    city.append(list(row))
    
    for j in range(c):
        if row[j] == "@":
            bender = Bender((j, i), "NORMAL", "NORMAL")
        elif row[j] == "$":
            suicide_cabin_position = (j, i)
            
        elif row[j] == "T":
            position_teleporteurs.append((j,i))

#Tant que Bender ne tourne pas en boucle et que la cabine à suicide n'a pas été trouvée
while(loop==False and suicide_cabin_found==False):
    direction_changed = ""
    next_cell = tuple()
    print(bender.position, file=sys.stderr)
    for direction in [bender.heading_to]+directions[bender.direction_priority]:
        next_cell = bender.find_where_to_head(directions_to_coordinates, direction, city)
        if next_cell is not None:
            bender.heading_to = direction
            break
            
    x, y = next_cell[0], next_cell[1]
    
    #Si bender tombe sur un modificateur de trajectoire : S, N, E, ou W
    if city[y][x] in directions_to_coordinates.keys():
        direction_changed = city[y][x]
                
    #Si bender tombe sur une bière
    elif city[y][x] == "B":
        bender.change_state()
                
    #Si bender tombe sur un inverseur de champs magnétique
    elif city[y][x] == "I":
        bender.change_direction_priority()
                
    #Si bender tombe sur un mur en mode casseur, il le casse
    elif city[y][x] == "X" and bender.state == "CASSEUR":
        city[y][x] = " "
            
    #Si bender tomber sur un téléporteur
    elif city[y][x] == "T":
        index_teleporteur = position_teleporteurs.index((x,y))
        if index_teleporteur == 0:
            next_cell = position_teleporteurs[1]
        else:
            next_cell = position_teleporteurs[0]
    
    bender.position = next_cell
    
    #Si Bender n'a pas encore visité la prochaine case, on l'ajoute aux cases déjà visitées
    if bender.position not in cell_already_visited:
        cell_already_visited.append(bender.position)
    else:
        nb_cell_already_visited += 1
        
    if nb_cell_already_visited == 100:
        loop = True
        
    #On ajoute la direction à la liste de directions
    bender.list_direction.append(direction_to_words[bender.heading_to])
    print(direction_to_words[bender.heading_to], file=sys.stderr)
    #Si la trajectoire a été modifiée par un modificateur de trajectoire, on change cette priorité dans bender
    if direction_changed != "":
        bender.heading_to = direction_changed

    #Si Bender tombe sur la cabine à suicide
    if bender.position == suicide_cabin_position:
        suicide_cabin_found = True
        
#Si loop est à True, on affiche LOOP, sinon on affiche les directions empruntées par Bender
if loop:
    print("LOOP")
else:
    for direction in bender.list_direction:
        print(direction)
