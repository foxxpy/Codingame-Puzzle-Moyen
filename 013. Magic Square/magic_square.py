import sys
import math

def est_un_entier(num):
    if "." in str(num):
        return False
    else:
        return True

#Instanciation des variables
n = int(input())
list_line = list()
list_different_number = list()
sum_line = []
not_magic = False

#On récupère les lignes
for i in range(n):
    line = list()
    for j in input().split():
        c = int(j)
        if c not in list_different_number:
            list_different_number.append(c)
            line.append(c)
        elif c in list_different_number or c < 1 or c > n**2 or not est_un_entier(c):
            not_magic = True
            break
    list_line.append(line)

for i in range(1, n**2+1):
    if i not in list_different_number:
        not_magic = True
        break

if not not_magic:
    #On calcule les sommes de chaque ligne et de chaque colonne
    for calculate_sum in ["line", "column"]:
        for i in range(n):
            sum_i_j = 0
            for j in range(n):
                if calculate_sum == "column":
                    sum_i_j += list_line[j][i]
                else:
                    sum_i_j += list_line[i][j]
                
            if sum_i_j not in sum_line:
                sum_line.append(sum_i_j)
    
    sum_i_j = 0
    #On calcule la somme pour la diagonale haut-gauche vers bas-droite
    for i in range(n):
        sum_i_j += list_line[i][i]
        if i == n - 1 and sum_i_j not in sum_line:
            sum_line.append(sum_i_j)
    
    sum_i_j = 0
    #On calcule la somme pour la diagonale bas-gauche vers haut-droite
    for i in range(n):
        sum_i_j += list_line[i][n-1-i]
        if i == n - 1 and sum_i_j not in sum_line:
            sum_line.append(sum_i_j)

if len(sum_line) > 1 or not_magic:
    print("MUGGLE")
else:
    print("MAGIC")