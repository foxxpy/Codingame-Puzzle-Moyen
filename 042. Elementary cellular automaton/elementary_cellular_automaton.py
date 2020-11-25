import sys
import math

def add_zeros(bin_i, max_length):
    """On ajoute des zéros au nombre binaire jusqu'à ce que sa taille soit celle de max_length"""

    while(len(bin_i) < max_length):
        bin_i = "0" + bin_i
    return bin_i

def set_rule(r):
    """On définit le dictionnaire rule qui va nous permettre d'évoluer"""
    binary_r = bin(r).replace("0b", "")
    binary_r = add_zeros(binary_r, 8)
    rule = dict()
    for i in range(0, 8):
        bin_i = bin(i).replace("0b", "")
        bin_i = add_zeros(bin_i, 3)
        rule[bin_i] = binary_r[-(i+1)]

    return rule

def translate_char_to_binary(pattern):
    """On traduit les caractères donnés dans l'énoncé en nombre binaire"""
    new_pattern = ""
    for char in pattern:
        if char == "@":
            new_pattern += "1"
        else:
            new_pattern += "0"

    return new_pattern

def translate_binary_to_char(pattern):
    """On traduit le nombre binaire dans les caractères donnés par l'énoncé"""
    start_pattern = ""
    for char in pattern:
        if char == "1":
            start_pattern += "@"
        else:
            start_pattern += "."

    return start_pattern

def create_new_pattern(rule, pattern):
    """On fait évoluer le pattern selon les règles établis dans le dictionnaire rule grâce à r"""
    new_pattern = ""
    for i in range(len(pattern)):
        indice = ""
        if i == 0:
            indice = pattern[-1]+pattern[i]+pattern[1]
        elif i == len(pattern) - 1:
            indice = pattern[-2]+pattern[-1]+pattern[0]
        else:
            for j in range(i-1, i+2):
                indice += pattern[j]

        new_pattern += rule[indice]
    return new_pattern


#Instanciation des variables
r = int(input())
n = int(input())
rule = set_rule(r)
start_pattern = input()

#On fait évoluer le pattern
for i in range(n):
    print(start_pattern)
    pattern = translate_char_to_binary(start_pattern)
    new_pattern = create_new_pattern(rule, pattern)
    start_pattern = translate_binary_to_char(new_pattern)



