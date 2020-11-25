import sys
import math

def decimalToBinary(n):
    """Transform a decimal number into a binary number in a string"""
    return bin(n).replace("0b", "")  

def binaryToLetters(binary):
    """Transform a binary number string in a full letters binary number"""
    binary_to_string = {"0" : "zero", "1" : "one"}
    string_binary = ""
    for num in binary:
        string_binary += binary_to_string[num]
       
    return string_binary

suite, n = [int(i) for i in input().split()]

#For the n-th term
for i in range(n):
    last_number = suite
    suite_binary = decimalToBinary(suite)
    string_binary = binaryToLetters(suite_binary)
    suite = len(string_binary)
   
    if last_number == suite:
        break


print(suite)