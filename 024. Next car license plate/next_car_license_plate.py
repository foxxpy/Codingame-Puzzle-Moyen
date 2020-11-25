import sys
import math

def calcul_nb_milieu(x, n):
    """Calcul du nombre central d'une plaque d'immatriculation"""
    nb_milieu = (int(x[1]) + n) % 999

    if nb_milieu < 10:
        nb_milieu = "00"+str(nb_milieu)
    elif nb_milieu < 100:
        nb_milieu = "0"+str(nb_milieu)
    else:
        nb_milieu = str(nb_milieu)

    return nb_milieu

def get_char_by_number(number):
    """Récupère une lettre de l'alphabet à partir d'un nombre"""
    list_char = []
    #On créé notre liste de lettres de l'alphabet en majuscule
    for i in range(26):
        list_char.append(chr(97+i).upper())

    #On choisit dans la liste des lettres de l'alphabet par rapport à l'indice de la lettre dans la liste
    number = number % 26

    return list_char[number]

#Instanciation des variables
x = input().split("-")
print("Plaque d'immatriculation de départ : "+str(x), file=sys.stderr)
n = int(input())
print("n : "+str(n), file=sys.stderr)

                        #----- Calcul de la nouvelle plaque -----
#Calcul du nombre du milieu
nb_milieu = calcul_nb_milieu(x, n)

#Calcul du dernier caractère : on avance par cycle de (x[1] + n) // 999 - 65
#Le 65 c'est la valeur de la lettre A dans la table ASCII que l'on redescend à 0
nb_dernier_caractere = ord(x[2][1]) + (int(x[1]) + n) // 999 - 65
dernier_caractere = get_char_by_number(nb_dernier_caractere)

#Calcul de l'avant-dernier caractère de la plaque
#On reprend le calcul de la dernière plaque et on a un cycle de 26 caractères
nb_avt_dernier_caractere = ord(x[2][0]) - 65 + nb_dernier_caractere // 26
avt_dernier_caractere = get_char_by_number(nb_avt_dernier_caractere)

#calcul_second_caractère
nb_second_caractere = ord(x[0][1]) - 65 + nb_avt_dernier_caractere // 26
second_caractere = get_char_by_number(nb_second_caractere)

#calcul_premiere_caractère
nb_premier_caractere = ord(x[0][0]) - 65 + nb_second_caractere // 26
premier_caractere = get_char_by_number(nb_premier_caractere)

print(premier_caractere+second_caractere+"-"+nb_milieu+"-"+avt_dernier_caractere+dernier_caractere)