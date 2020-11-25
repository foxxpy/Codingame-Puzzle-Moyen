import sys
import math


#Instanciation des variables
n = int(input())
list_w = list()
results = dict()

pt_letter = {"aeionrtlsu" : 1,
"dg" : 2,
"bcmp" : 3,
"fhvwy" : 4,
"k" : 5,
"jx" : 8,
"qz" : 10}

#On ajoute chaque mot à notre liste de mots : list_w
for i in range(n):
    w = input()
    list_w.append(w)
print(list_w, file=sys.stderr)
letters = input()

#Pour chaque mot dans notre liste de mots, on regarde si les lettres qui le composent sont dans la
#liste des lettres qui nous ont été données
for word in list_w:
    total_point = 0
    copy_letters = letters[:] #Lettres données pour la partie
    invalid_word = False

    #Pour chaque lettre d'un mot
    for letter_word in word:
        if not letter_word in copy_letters: #On regarde si elles ne sont dans copy_letters
            invalid_word = True
            break
        else: #Si elles y sont, on cherche la valeur en points de la lettre et on retire la lettre de copy_letters
            for key, value in pt_letter.items():
                if letter_word in key:
                    total_point += pt_letter[key]
                    copy_letters = copy_letters.replace(letter_word, "", 1)
    
    if not invalid_word:
        results.update({word : total_point})

max_point = max(results, key=results.get)
print(max_point)
