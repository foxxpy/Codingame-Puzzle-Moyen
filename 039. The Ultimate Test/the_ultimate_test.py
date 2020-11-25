import sys
import math

def solve(n, k, temp="", level=0):
    #On récupère le nombre dans n à la position level
    temp += n[level]

    #Si on arrive à la fin de n, on effectue les calculs dans temp pour voir si c'est égal à k
    if level == len(n) - 1:
        total = 0
        i = 0
        j = 0
        positive = True

        #Tant que j n'est pas égal à + ou -, on l'incrémente. Dés qu'on tombe sur un signe
        #On effectue le calcul avec le signe qu'on a eu avant (contenu dans le booléen positive)
        #Et on garde en mémoire le signe pour le chiffre suivant à ajouter
        while(i < len(temp)):
            if j == len(temp) or temp[j] in ["+", "-"]:
                if positive:
                    total += int(temp[i:j])
                else:
                    total -= int(temp[i:j])

                if j < len(temp) and temp[j] == "+":
                    positive = True
                else:
                    positive = False
                i = j + 1
            j = j + 1

        #Si le total est égal à k, on l'ajoute aux solutions
        if total == k:
            solutions.append(temp)

        return
         
    for i in ["", "+", "-"]:
        temp += i
        solve(n, k, temp, level+1)
        if i != "":
            temp = temp[0:-1]

#Instanciation des variables
n = input()
k = int(input())
solutions = []

solve(n, k)

#On affiche les solutions
for solution in solutions:
    print(solution)
