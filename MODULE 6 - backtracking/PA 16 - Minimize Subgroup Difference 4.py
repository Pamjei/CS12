#GUMANA KA RIN HINAYUPAK KA!!!
from itertools import combinations
from collections import Counter
import sys

N = int(input())
for i in range(N):
    entry = input().split()
    x = int(input())
    values = []
    for i in range(0,len(entry),3):
        a,b,c = int(entry[i]),int(entry[i+1]),int(entry[i+2])
        values.append(a*(x**2) + b*x + c)
    total = sum(values)
    partition = len(values)//2
    minn = sys.maxsize
    combi = list(combinations(values,partition))
    for tup in combi:
        if values[0] in tup:
            complement = tuple(Counter(values) - Counter(tup))
            if abs(sum(tup)-sum(complement)) < minn:
                minn = abs(sum(tup)-sum(complement))
                sub1 = tup
                sub2 = complement
    print(" ".join(str(x) for x in sub1+sub2))
