import sys
import math

def block_or_wait(clone_pos, clone_floor, object_pos, list_blocked_floor):
    if (clone_pos < object_pos and direction == "LEFT") or (clone_pos > object_pos and \
    direction == "RIGHT") and list_blocked_floor[clone_floor] == False:
        return "BLOCK"
    else:
        return "WAIT"
    
# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
list_blocked_floor = [False for _ in range(nb_floors)]

dict_elevator = dict()

#On ajoute la position des ascenceurs à dict_elevator
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    dict_elevator[elevator_floor] = elevator_pos


# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    decision = ""
    
    #On regarde si le clone de tête se situe sur un étage où il y'a un ascenceur
    if clone_floor in dict_elevator.keys():
        decision = block_or_wait(clone_pos, clone_floor, dict_elevator[clone_floor], list_blocked_floor)
    
    #On regarde si le clone de tête est à l'étage de la sortie
    elif clone_floor == exit_floor:
        decision = block_or_wait(clone_pos, clone_floor, exit_pos, list_blocked_floor)
            
    else:
        decision = "WAIT"
        
    #Si on décide de bloquer un clone, on indique qu'à cet étage un clone est déjà bloqué
    if decision == "BLOCK":
        list_blocked_floor[clone_floor] = True
    print(decision)
