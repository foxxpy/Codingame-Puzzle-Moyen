import sys
import math

def calculate_number(num, length_num, s, number_of_zeros):
    for i in range(length_num):
        if (i == 0 or i>0 and number_of_zeros == 0) and len(s):
            num += str(min(s))
            s.remove(min(s))
        elif i > 0 and number_of_zeros > 0:
            num += "0"
            number_of_zeros -= 1  
            
    return num, number_of_zeros
    
def fill_number_with_zeros(num, number_of_zeros, number_of_zeros_to_set, s):
    #Si number_of_zeros_to_set = 1, alors on est dans le cas où le nombre vaudra 0.
    #Donc on ne recherche pas de chiffre dans s
    num = ""
    num += str(min(s)) if number_of_zeros_to_set > 1 else ""
    num += "0" * number_of_zeros_to_set
    if number_of_zeros_to_set > 1:
        s.remove(min(s))
    number_of_zeros -= number_of_zeros_to_set
    
    return num, number_of_zeros
    
def optimize_numbers(length_a, length_b, s, number_of_zeros):
    a, b = "", ""
    s = s[:]
    b_already_set = False
    a_already_set = False

    #Cas où b peut valoir 10**18
    if length_b == 19 and number_of_zeros >= 18:
        b, number_of_zeros = fill_number_with_zeros(b, number_of_zeros, 18, s)
        b_already_set = True

    #Cas où a peut valoir 10**18
    if length_a == 19 and number_of_zeros >=18:
        a, number_of_zeros = fill_number_with_zeros(a, number_of_zeros, 18, s)
        a_already_set = True
     
    #Cas où a peut valoir 0
    if length_a == 1 and number_of_zeros > 0:
        a, number_of_zeros = fill_number_with_zeros(a, number_of_zeros, 1, s)
        a_already_set = True
        
    #Cas où b peut valoir 0
    if length_b == 1 and number_of_zeros > 0:
        b, number_of_zeros = fill_number_with_zeros(b, number_of_zeros, 1, s)
        b_already_set = True
    
    if not a_already_set:  
        a, number_of_zeros = calculate_number(a, length_a, s, number_of_zeros)
                
    if not b_already_set:
        b, number_of_zeros = calculate_number(b, length_b, s, number_of_zeros)
        
    return a, b

def calculate_length_number(length_s):
    """On maximise la longueur de b et on minimise la longueur de a"""
    if length_s >= 20:
        length_b = 19
        length_a = length_s - length_b
    else:
        length_a = 1
        length_b = length_s - length_a
            
    return length_a, length_b


def find_zeros_in_list_and_remove_them(s):
    number_of_zeros = 0
    while 0 in s:
        s.remove(0)
        number_of_zeros += 1
        
    return number_of_zeros
    
#Instanciation des variables
s = list(input())
print("".join(s), file=sys.stderr)
s = [int(x) for x in s]
length_s = len(s)
s.sort()
number_of_zeros = find_zeros_in_list_and_remove_them(s)
a, b = "-1", "-1"
find_result = False

only_zeros = True if len(s) == 0 and length_s > 2 else False
not_enough_digits = True if length_s > 20 and number_of_zeros == length_s - 1 else False

#Si la longueur de s est supérieure à 38, alors on ne peut pas créer deux chiffres
#inférieurs ou égaux à 10**18
if length_s <= 38 and length_s > 1 and not only_zeros and not not_enough_digits:
    length_a, length_b = calculate_length_number(length_s)
    print(length_a, length_b, file=sys.stderr)

    #Tant que le nombre de chiffres de a ne dépasse pas le nombre de chiffre total
    #et qu'on a pas encore trouvé de résultat valide
    while (length_a <= length_b and not find_result):
        find_result = True
        a, b = optimize_numbers(length_a, length_b, s, number_of_zeros)


        #Conditions qui font que le résultat n'est pas convenable
        if a == "" or b == "" or \
            int(a) == 0 and len(a) > 1 or int(b) == 0 and len(b) > 1 or \
            int(b) > 10**18 or int(a) > 10**18 or\
            length_b < length_a or int(b) < int(a):
            find_result = False
        length_a += 1
        length_b -= 1
        
if find_result:
    print(a+" "+b)
else:
    print("-1 -1")
    

