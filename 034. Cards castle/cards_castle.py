import sys
import math

#Instanciation des variables
stable = True
h = int(input())
cards = []

#On récupère les lignes
for i in range(h):
    s = input()
    cards.append(s)
    if "//" in s or "\\\\" in s or "/." in s or ".\\" in s:
        stable = False
    print(s, file=sys.stderr)

#On parcourt les lignes
for i in range(h):
    for j in range(h*2):
        if i+1 < h and cards[i][j] == "\\" and cards[i+1][j] in ["\\", "."]:
            stable = False
        if i+1 < h and cards[i][j] == "/" and cards[i+1][j] in ["/", "."]:
            stable = False
if stable:
    print("STABLE")
else:
    print("UNSTABLE")