import sys
import math

def sum_matrix(matrix1, matrix2):
    """Calcul la somme des deux matrices"""
    final_matrix = []
    for i, row_matrix1 in enumerate(matrix1):
        final_row = int(row_matrix1) + int(matrix2[i])
        if final_row < 10:
            final_row = "00"+str(final_row)
        elif final_row < 100:
            final_row = "0"+str(final_row)
        else:
            final_row = str(final_row)
        final_matrix.append(list(final_row))

    return final_matrix

def distribute_sand(matrix, i, j):
    """On ajoute les grains de sable sur les cases alentours"""
    if i+1 < len(matrix):
        matrix[i+1][j] = str(int(matrix[i+1][j]) + 1)
    if j+1 < len(matrix[0]):
        matrix[i][j+1] = str(int(matrix[i][j+1]) + 1)
    if i-1 >= 0:
        matrix[i-1][j] = str(int(matrix[i-1][j]) + 1)  
    if j-1 >= 0:
        matrix[i][j-1] = str(int(matrix[i][j-1]) + 1)
    matrix[i][j] = str(int(matrix[i][j]) - 4) 
    return matrix

def reduce_sandpile(matrix):
    """On réduit la pile de sable et tant qu'on a trouvé des nombres supérieurs à 3
    on continue de vérifier la matrice pour voir si il n'y a pas du sable à distribuer"""
    sandpile = True
    while(sandpile):
        sandpile = False
        for i, line in enumerate(matrix):
            for j, col in enumerate(line):
                if int(col) > 3:
                    matrix = distribute_sand(matrix, i, j)
                    sandpile = True
    return matrix

#Instanciation des variables
n = int(input())
matrix1 = list()
matrix2 = list()
for i in range(n):
    row = input()
    matrix1.append(row)

for i in range(n):
    row = input()
    matrix2.append(row)

final_matrix = sum_matrix(matrix1, matrix2)
final_matrix = reduce_sandpile(final_matrix)

#Affichage du résultat
for row in final_matrix:
    print("".join(row))
