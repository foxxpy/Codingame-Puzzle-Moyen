import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
sum_d = 0
print("n : "+str(n), file=sys.stderr)
for i in range(1,n+1):
    sum_d += (n // i) * i

print(sum_d)
