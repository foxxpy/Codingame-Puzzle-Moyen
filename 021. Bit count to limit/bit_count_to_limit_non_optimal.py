import sys
import math

#Instanciation des variables
n = int(input())
total_ones = 0

for i in range(n+1):
    print(bin(i), file=sys.stderr)
    total_ones += bin(i)[2:].count("1")

print(total_ones)