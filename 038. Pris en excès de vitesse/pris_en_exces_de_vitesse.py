import sys
import math

#Instanciation des variables
speed_limit = int(input())
n = int(input())
vehicles = dict()
exces_de_vitesse = False

#Pour chaque véhicule on les ajoute au dictionnaire, et on calcule leur vitesse par rapport au passage
#à un poste de contrôle précédent (r[0] : matricule, r[1] : km, r[2] : timestamp)
for i in range(n):
    r = input().split(" ")

    if r[0] in vehicles.keys():
        time = int(r[2]) - int(vehicles[r[0]][1]) #temps entre cette photo et celle d'avant
        distance = int(r[1]) - int(vehicles[r[0]][0]) #distance entre cette photo et celle d'avant
        speed = (distance / time) * 3600 #calcul de la vitesse en km/h
        if speed > speed_limit:
            print(r[0], r[1])
            exces_de_vitesse = True

    vehicles[r[0]] = [r[1], r[2]]

if not exces_de_vitesse:
    print("OK")