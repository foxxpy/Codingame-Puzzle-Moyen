import sys
import math

def print_list_of_nodes(list_of_nodes):
    for node in list_of_nodes:
        print("--------------------------", file=sys.stderr)
        print("Node num : "+str(node.num), file=sys.stderr)
        print("Node distance from start point : "+str(node.distance_from_start_point), file=sys.stderr)
        if node.pere is None:
            print("Pas de père", file=sys.stderr)
        else:
            print("Num du père : "+str(node.pere.num), file=sys.stderr)

def initialisation_list_of_nodes(list_of_nodes, n):
    """Initialisation de la liste des noeuds pour le parcours en largeur"""
    for node in list_of_nodes:
        node.status = 0
        node.distance_from_start_point = n+1
        node.pere = None

def parcours_en_largeur(skynet, list_of_nodes):
    """Algorithme de parcours en largeur indiquant les distances de chaque noeud par rapport à la position de Skynet"""
    queue = [skynet]
    skynet.status = 1
    skynet.distance_from_start_point = 0
    
    while(len(queue) > 0):
        node_to_analyze = queue[0]
        for node in node_to_analyze.connected_to:
            if node.status == 0:
                node.pere = node_to_analyze
                node.distance_from_start_point = queue[0].distance_from_start_point + 1
                node.status = 1
                queue.append(node)
        queue.pop(0)
        node_to_analyze.status = 2

def find_link_to_cut(list_of_nodes, node):
    """On remonte le graphe obtenu par le parcours en largeur pour trouver le premier lien à couper"""
    while(node.pere is not None):
        link_to_cut = (node.pere, node)
        node = node.pere
    
    return link_to_cut

class Node:
    def __init__(self, num):
        self.num = num
        self.connected_to = list()
        self.status = 0
        self.distance_from_start_point = 0
        self.pere = None
        
    def set_connected_to(self, other_node):
        """Connecte ce noeud à un autre noeud"""
        self.connected_to.append(other_node)
        
    def about_me(self):
        print("Node num : "+str(self.num), file=sys.stderr)
        print("Distance from start point : "+str(self.distance_from_start_point), file=sys.stderr)

#Instanciation des variables
n, l, e = [int(i) for i in input().split()]
list_of_nodes = list()
list_of_exit = list()


#On créé nos noeuds et on les ajoute à notre liste de noeuds
for i in range(n):
    list_of_nodes.append(Node(i))


#N1 et N2 définissent les liens entre les noeuds
#On définit les liens entre les noeuds par leur attribut connected_to
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    node1 = next(filter(lambda x: x.num == n1, list_of_nodes))
    node2 = next(filter(lambda x: x.num == n2, list_of_nodes))
    node1.set_connected_to(node2)
    node2.set_connected_to(node1)    
    #print("(n1, n2) : ("+str(n1)+", "+str(n2)+")", file=sys.stderr)


# ei : l'index d'un noeud de sortie
for i in range(e):
    ei = int(input())
    list_of_exit.append(ei)


# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    link_to_cut = tuple()
    distance_min = n+1
    
    #On parcours le graphe en largeur pour déterminer la plus courte distance entre skynet et exit
    for exit in list_of_exit:
        node_skynet = next(filter(lambda x: x.num == si, list_of_nodes))
        initialisation_list_of_nodes(list_of_nodes, n)
        parcours_en_largeur(node_skynet, list_of_nodes)
        node_exit = next(filter(lambda x: x.num == exit, list_of_nodes))

        #Si le node de la sortie est le plus prôche actuellement de Skynet, on retient sa distance et on calcule 
        #le lien à couper pour bloquer Skynet
        if node_exit.distance_from_start_point < distance_min:
            distance_min = node_exit.distance_from_start_point
            link_to_cut = find_link_to_cut(list_of_nodes, node_exit)
            
    link_to_cut[0].connected_to.remove(link_to_cut[1])
    link_to_cut[1].connected_to.remove(link_to_cut[0])            
    link_to_cut_str = str(link_to_cut[0].num)+" "+str(link_to_cut[1].num)
    
    # On affiche le lien à couper
    print(link_to_cut_str)
