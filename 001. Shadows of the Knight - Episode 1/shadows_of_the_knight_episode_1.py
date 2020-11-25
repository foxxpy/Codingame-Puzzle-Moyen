import sys
import math

#Instanciation des variables
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
w0, h0 = 0, 0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if "U" in bomb_dir:
        h = y0
        y0 = math.floor((y0 + h0) / 2)
    
    if "R" in bomb_dir:
        w0 = x0
        x0 = math.floor((x0 + w) / 2)
        
    if "L" in bomb_dir:
        w = x0
        x0 = math.floor((x0 + w0) / 2)
        
    if "D" in bomb_dir:
        h0 = y0
        y0 = math.floor((y0 + h) / 2)

    # the location of the next window Batman should jump to.
    print(str(int(x0))+" "+str(int(y0)))