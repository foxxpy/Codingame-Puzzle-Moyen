import sys
import math

def find_sub_sequence(list_int):
    """Comme la liste est triée, on regarde si l'élément suivant est égale à l'élément n additionné de 1
    Si c'est le cas, on ajoute les deux élements et on considère qu'on entre dans une sous-séquence"""
    max_sequence = 0
    return_sequence = []
    temp_subsequence = []
    found_subsequence = False
    for i, t in enumerate(list_int):
        if i+1 < len(list_int) and list_int[i+1][1] - t[1] == 1 and list_int[i+1][0] > t[0]:
            if not found_subsequence:
                found_subsequence = True
                temp_subsequence.append(t[1])
                temp_subsequence.append(list_int[i+1][1])
            else:
                temp_subsequence.append(list_int[i+1][1])

        else:
            found_subsequence = False
            if len(temp_subsequence) > max_sequence:
                max_sequence = len(temp_subsequence)
                return_sequence = temp_subsequence
            temp_subsequence = []

    return return_sequence



#Instanciation des variables
n = int(input())
list_int = []

#Récupération des nombres
for i, num in enumerate(input().split()):
    l = int(num)
    list_int.append((i, l))

list_int.sort(key=lambda t: t[1])

#On retire les nombres en double en supprimant celui qui a l'index dans la liste le moins élevé
i = 0
while(i < len(list_int)):
    if i+1 < len(list_int) and list_int[i][1] == list_int[i+1][1]:
        if list_int[i][0] < list_int[i+1][0]:
            list_int.remove(list_int[i])
        else:
            list_int.remove(list_int[i+1])
    else:
        i = i + 1


sub_sequences = find_sub_sequence(list_int)

print(" ".join([str(x) for x in sub_sequences]))
