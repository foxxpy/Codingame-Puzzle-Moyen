import sys
import math

#Instanciation des variables
n = int(input())
list_x = list()
num_swap = 0

#On récupère nos nombres
for i in input().split():
    x = int(i)
    list_x.append(x)

reversed_list_x = list_x[::-1]

while(1 in list_x):
    if list_x[0] == 0:
        index_one = reversed_list_x.index(1)
        list_x[len(list_x) - 1 - index_one] = 0
        reversed_list_x[index_one] = 0
        num_swap += 1
        
    list_x.pop(0)
    
print(num_swap)