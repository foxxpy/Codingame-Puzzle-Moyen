import sys
import math



class Langton:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        


    def set_next_direction(self, color):
        """Défini la nouvelle direction dans laquelle regarde la fourmi suivant le type de case où elle est arrivée"""
        rotation = "clockwise" if color == "#" else "counter-clockwise"
        directions = {
            "clockwise" : {
                "N" : "E",
                "E" : "S",
                "S" : "W",
                "W" : "N"
            },
            "counter-clockwise" : {
                "N" : "W",
                "W" : "S",
                "S" : "E",
                "E" : "N"
            }
        }

        self.direction = directions[rotation][self.direction]



    def set_next_position(self):
        direction_position = {
            "N" : (0, -1),
            "S" : (0, 1),
            "W" : (-1, 0),
            "E" : (1, 0)
        }

        move = direction_position[self.direction]
        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]
        self.position = (new_x, new_y)



#Instanciation des variables
w, h = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]
print("Initial position : "+str((x, y)), file=sys.stderr)
direction = input()
print("Initial direction : "+str(direction), file=sys.stderr)
t = int(input())
grid = list()
ant = Langton((x,y), direction)


#On récupère la grille
for i in range(h):
    c = list(input())
    grid.append(c)


#On déplace la fourmi
for i in range(t):
    #On récupère la couleur de la case où est la fourmi, on change sa direction et sa position
    ant_x, ant_y = ant.position[0], ant.position[1]
    color = grid[ant_y][ant_x]
    ant.set_next_direction(color)
    ant.set_next_position()

    #On change la couleur de la case précédente
    grid[ant_y][ant_x] = "." if color == "#" else "#"

#On affiche la grille finale
for line in grid:
    print("".join(line))
