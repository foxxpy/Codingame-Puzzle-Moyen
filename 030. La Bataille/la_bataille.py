import sys
import math

#Instanciation des variables
tas_p1 = []
tas_p2 = []
values = {
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 11,
    "Q" : 12,
    "K" : 13,
    "A" : 14
}
bataille = False #Indique si une bataille est en cours
exaequo = False

#On récupère les cartes du joueur 1
n = int(input())
for i in range(n):
    cardp_1 = input()
    tas_p1.append(cardp_1[0:-1])
print("Cartes p1 : "+str(tas_p1), file=sys.stderr)

#On récupère les cartes du joueur 2
m = int(input())
for i in range(m):
    cardp_2 = input()
    tas_p2.append(cardp_2[0:-1])
print("Cartes p2 : "+str(tas_p2), file=sys.stderr)

#Tant que les 2 joueurs ont encore des cartes
nb_manches = 0
defausse_p1 = []
defausse_p2 = []
while(len(tas_p1) > 0 and len(tas_p2) > 0 and not exaequo):
    card_p1 = tas_p1.pop(0)
    card_p2 = tas_p2.pop(0)

    #Si la valeur de la carte du joueur 1 est supérieure à celle du joueur 2
    if values[card_p1] > values[card_p2]:
        tas_p1 += defausse_p1 + [card_p1] + defausse_p2 + [card_p2]
        nb_manches += 1
        defausse_p1 = []
        defausse_p2 = []

    #Si la valeur de la carte du joueur 2 est supérieure à celle du joueur 1
    elif values[card_p2] > values[card_p1]:
        tas_p2 += defausse_p1 + [card_p1] + defausse_p2 + [card_p2]
        nb_manches += 1
        defausse_p1 = []
        defausse_p2 = []

    #Si c'est une bataille : donc quand les cartes des deux joueurs ont la même valeur
    else:
        if len(tas_p1) < 4 or len(tas_p2) < 4:
            exaequo = True

        else:
            defausse_p1 += [card_p1] + [tas_p1.pop(0)] + [tas_p1.pop(0)] + [tas_p1.pop(0)]
            defausse_p2 += [card_p2] + [tas_p2.pop(0)] + [tas_p2.pop(0)] + [tas_p2.pop(0)]

if exaequo:
    print("PAT")
else:
    winner = 1 if len(tas_p2) == 0 else 2
    print(winner, nb_manches)

