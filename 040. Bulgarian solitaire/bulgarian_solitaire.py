import sys
import math

#Instanciation des variables
n = int(input())
pile = list()
piles_already_seen = list()

#On récupère les premières piles
for i in input().split():
    c = int(i)
    pile.append(c)

#On enlève les zéros de la pile
pile = [value for value in pile if value > 0]

#Tant qu'on a pas rencontré une pile que l'on a déjà rencontré avant
while(not pile in piles_already_seen):
    piles_already_seen.append(pile[:])
    pile = []
    num_card = 0

    #On enlève une carte par pile et on compte combien de cartes on enlève pour connaître le nombre
    #de cartes du nouveau tas
    for p in piles_already_seen[-1]:
        pile.append(p-1)
        num_card += 1

    pile.append(num_card)
    
    pile = [value for value in pile if value > 0] #On ne garde pas les tas de 0 carte
    pile.sort()

#On calcule la distance entre les deux piles similaires
length = len(piles_already_seen) - piles_already_seen.index(pile)
print(length)
