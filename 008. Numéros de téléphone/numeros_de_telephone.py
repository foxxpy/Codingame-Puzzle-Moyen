import sys
import math

def check_node(list_num, nb_node = 0):
    dict_num = dict()
    
    #Pour chaque numéro, on ajoute son premier chiffre en clé de dictionnaire
    for num in list_num:
        
        #On récupère le premier chiffre et on l'associe aux chiffres restants du numéro
        if len(num) > 0 and num[0] not in dict_num.keys():
            dict_num.update( {num[0] : [num[1:]]} )
            nb_node += 1
        
        #Si le premier chiffre est déjà dans le dictionnaire, on ajoute le numéro à la liste de numéros
        #associée à ce chiffre
        elif len(num) > 0 and num[0] in dict_num.keys():
            dict_num[num[0]].append(num[1:])
    
    #Pour chaque clé du dictionnaire (donc chaque noeud), on envoie la liste des chiffres restant
    #dans les numéros qui lui sont associés
    for key, value in dict_num.items():
        if dict_num[key] != [""]:
            nb_node += check_node(value)
            
    return nb_node

n = int(input())
list_telephone = list()

#On récupère la liste des numéros de téléphone
for i in range(n):
    telephone = input()
    list_telephone.append(telephone)
    list_telephone.sort()

nb_node = check_node(list_telephone)
print(nb_node)