import sys
import math

#Instanciation des variables
#On associe la valeur des chiffres et des lettres à leur valeur en int
value = {}
for i in range(10):
    value[str(i)] = i
for i in range(65, 91): #On ajoute les lettres au dictionnaire de valeurs
    value[chr(i)] = i - 55

max_num = 0
equality = input()
num1, num2 = equality.split("+")
num2, result = num2.split("=")

#La première étape est de récupérer le chiffre maximal qui nous dira
#par quel système commencer
max_num = max(list(num1)+ list(num2)+list(result))
first_system = value[max_num]+1

#Tant qu'on n'a pas trouvé le bon système qui résoud l'égalité, on continue en passant au
#système supérieur
solved = False
while(not solved):
    num = num2 if len(num1) < len(num2) else num1
    other_num = num1 if num == num2 else num2
    sum_digit = 0

    #On calcule la somme des deux nombres en partant d'un système hypothétique vers le système décimal
    for i, digit in enumerate(num[::-1]):
        if i < len(other_num):
            pos_other_num = len(other_num) - i - 1
            sum_digit += (value[digit] + value[other_num[pos_other_num]]) * first_system**i
        else:
            sum_digit += value[digit] * first_system**i

    #On calcule le résultat dans le système décimal
    decimal_result = 0
    for i, digit in enumerate(result[::-1]):
        decimal_result += value[digit] * first_system**i

    #Si l'égalité est vraie dans le système décimal, alors ce système est le bon
    if sum_digit == decimal_result:
        solved = True
    else:
        first_system += 1

print(first_system)