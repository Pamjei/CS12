import math
from fractions import Fraction 

N = int(input())
num = input().split(" ")
denom = input().split(" ")
num = [int(i) for i in num]
denom = [int(i) for i in denom]
fractions = []
for x in range(N):
    frac = Fraction(num[x],denom[x])
    fractions.append(frac)
print(fractions.sort())
