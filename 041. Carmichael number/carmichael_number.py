import sys
import math

def is_prime(n):
    """On teste si le nombre n est un nombre premier, en calculant le modulo avec des valeurs pour i allant
    de 2 à n // 4"""
    for i in range(2, n//4):
        if n % i == 0:
            return False

    return True

def is_carmichael(n):
    """On teste pour voir si l'égalité donnée dans l'énoncé marche sur les 20 premiers nombres"""
    for i in range(1,20):
        if i**n%n != i % n:
            return False
    return True

#Instanciation des variables
n = int(input())
prime = is_prime(n)
carmichael = False

#Si le nombre n'est pas un nombre premier, on teste si c'est un nombre de carmichael
if not prime:
    carmichael = is_carmichael(n)

#Résultat final
if carmichael:
    print("YES")
else:
    print("NO")
