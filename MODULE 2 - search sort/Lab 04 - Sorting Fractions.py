import math

N = int(input())
num = input().split(" ")
denom = input().split(" ")
num = [int(i) for i in num]
denom = [int(i) for i in denom]
fractions = []
decimals = []
for x in range(N):
    gcd = math.gcd(num[x],denom[x])
    New_num = int(num[x]/gcd)
    New_denom = int(denom[x]/gcd)
    if New_denom < 0:
        New_denom = New_denom*(-1)
        New_num = New_num*(-1)
    fractions.append(str(New_num)+'/'+str(New_denom))

for y in range(N):
    decimals.append(eval(fractions[y]))

zipped_lists = zip(decimals, fractions)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
decimals, fractions = [ list(tuple) for tuple in  tuples]
print(fractions)

print(" ".join(str(x) for x in fractions))
