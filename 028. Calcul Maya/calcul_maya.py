import sys
import math

def maya_to_decimal(maya, maya_num):
    """Convertit un nombre maya en nombre décimal"""
    decimal = 0
    for i, maya_digit in enumerate(maya_num):
        for key, value in maya.items():
            if maya_digit == value:
                decimal += key * 20 ** (len(maya_num) - (i+1))

    return decimal

def decimal_to_maya(maya, num):
    """Convertit un nombre décimal en nombre maya"""
    if num == 0:
        return [maya[0]]

    else:
        maya_num = []
        i = 1
        #On cherche entre quelles puissances de 20 est compris le nombre décimal
        while(not 20**(i-1) <= num < 20**(i)):
            i = i + 1

        for j in range(i-1, -1, -1):
            digit = num // (20**j)
            num = num % (20**j)
            maya_num.append(maya[digit])
        
        return maya_num


def apply_operation(num1, num2, operation):
    """On applique l'opération qui nous est donnée entre les deux nombres décimaux obtenus
    à partir des nombres mayas"""
    
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    else:
        return num1 // num2

l, h = [int(i) for i in input().split()]
num1_maya = []
num2_maya = []

#On instancie un dictionnaire qui récupèrera les nombres Mayas
maya = dict()
for i in range(20):
    maya[i] = []

#On récupère les chiffres Mayas dans un dictionnaire
for i in range(h):
    numeral = input()
    for j in range(0, 20):
        maya[j].append(numeral[j*l:j*l+l])

#On récupère la transcription maya du premier nombre
s1 = int(input())
digit_maya = []
for i in range(s1):
    num_1line = input()
    digit_maya.append(num_1line)
    if (i+1) % l == 0:
        num1_maya.append(digit_maya)
        digit_maya = []

#On récupère la transcription maya du second nombre
s2 = int(input())
digit_maya=[]
for i in range(s2):
    num_2line = input()
    digit_maya.append(num_2line)
    if (i+1) % l == 0:
        num2_maya.append(digit_maya)
        digit_maya = []

#On convertit les nombres mayas en nombres décimaux
num1_decimal = maya_to_decimal(maya, num1_maya)
num2_decimal = maya_to_decimal(maya, num2_maya)

#On execute l'opération sur les nombres décimaux
operation = input()
final_result = apply_operation(num1_decimal, num2_decimal, operation)

#On reconvertit le nombre obtenu après l'opération en chiffre maya
final_maya = decimal_to_maya(maya, final_result)
for digit in final_maya:
    for digit_line in digit:
        print(digit_line)
