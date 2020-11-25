import sys
import math

#Instanciation des variables
n = int(input())
c = int(input())
list_b = list()
total_money = 0
print("Prix du cadeau : "+str(c), file=sys.stderr)
print("Nombre de personne : "+str(n), file=sys.stderr)

for i in range(n):
    b = int(input())
    list_b.append({"b" : b, "pay" : 0})
    total_money += b

list_final = sorted(list_b, key = lambda x: x['b']) 

#Si les personnes ont le budget pour le cadeau
if total_money >= c:
    
    #Tant qu'il reste de l'argent à mettre pour financer le cadeau
    while (c > 0):
        moy_per_person = math.floor(c/n) if math.floor(c/n) != 0 else math.ceil(c/n)

        for budget in list_final:
            #Si le budget d'une personne est inférieure à la moyenne que chaque personne doit payer
            #Elle donne la totalité de son budget
            if 0 < budget["b"] < moy_per_person:
                c -= budget["b"]
                budget["pay"] += budget["b"]
                budget["b"] = 0
                
            #Sinon la personne paie la moyenne par personne pour le cadeau
            elif budget["b"] >= moy_per_person and c > 0:
                c -= moy_per_person
                budget["b"] -= moy_per_person
                budget["pay"] += moy_per_person
            
    list_final = sorted(list_final, key = lambda x : x["pay"])

    for person in list_final:
        print(person["pay"])
        
        
#Si les personnes n'ont pas le budget pour le cadeau
else:
    print("IMPOSSIBLE")

    #Tant qu'il reste de l'argent à mettre pour financer le cadeau

            #Si le budget d'une personne est inférieure à la moyenne que chaque personne doit payer
            #Elle donne la totalité de son budget


            #Sinon la personne paie la moyenne par personne pour le cadeau
