import sys
import math

#Instanciation des variables
n = int(input())
y = int(input())
porcupine_datas = list()

#On récupère les informations concernant les cages des porc-épics
for i in range(n):
    s, h, a = [int(j) for j in input().split()]
    porcupine_datas.append({"s" : s, "h" : h, "a" : a})

print(porcupine_datas, file=sys.stderr)

#A chaque année qui passe
for i in range(y):
    #Pour chaque cage de porc-épic
    for j in range(n):
        porcupine_datas[j]["a"] -= porcupine_datas[j]["s"]
        porcupine_datas[j]["s"] = porcupine_datas[j]["s"]*2
        porcupine_datas[j]["h"] -= porcupine_datas[j]["s"]
        
    total_porcupines_alive = 0
    for j in range(n):
        if porcupine_datas[j]["a"] > 0:
            total_porcupines_alive += porcupine_datas[j]["a"]
    
    if total_porcupines_alive <= 0:
        print("0")
        break
    else:
        print(total_porcupines_alive)