import sys
import math

#Instanciation des variables
n1, n2 = [int(i) for i in input().split()]
s1 = input()
s2 = input()
t = int(input())
time = 0 #Placement des fourmis à l'instant t
line_ants = s1[::-1] + s2 #Ligne de fourmis

#Tant que l'instant time est inférieur au t-ème temps
while(time < t):
    i = 0
    while(i < len(line_ants)):
        #Si une fourmi fait parti du premier groupe et que juste après elle
        #Il y'a une fourmi du second groupe, on les échange
        if i+1 < len(line_ants) and line_ants[i] in s1 and line_ants[i+1] in s2:
            line_ants = line_ants[0:i]+line_ants[i+1]+line_ants[i]+line_ants[i+2:]
            i = i + 2
        else:
            i = i + 1
    time = time + 1

#Affichage du résultat
print(line_ants)
