import sys
import math

#Instanciation des variables
n = int(input())
total_1s = bin(n).replace("0b", "").count("1")
n_term = 1
i = 0

while (n != 0):
    if not 2**i <= n < 2**(i+1):
        if i != 0:
            n_term = 2*n_term + 2**(i-1)
        total_1s += n_term
        i = i + 1
    else:
        total_1s += n - 2**i
        n = n % 2**i
        n_term = 1
        i = 0

print(total_1s)
