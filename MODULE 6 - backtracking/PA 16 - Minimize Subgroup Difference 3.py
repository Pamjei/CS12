#MLE tc10 67mb

from itertools import combinations
import sys

N = int(input())
for i in range(N):
    entry = input().split()
    x = int(input())
    values = []
    for i in range(0,len(entry),3):
        a,b,c = int(entry[i]),int(entry[i+1]),int(entry[i+2])
        values.append(a*(x**2) + b*x + c)
    partition = len(values)//2 #how many elements in each tup
    minn = sys.maxsize
    for j, k in list(combinations(combinations(values,partition),2)):
        if len(set(values)) == len(values):
            if abs(sum(j) - sum(k)) < minn and all(x not in j for x in k):
                minn = abs(sum(j) - sum(k))
                finalj = j
                finalk = k
        else:
            if abs(sum(j) - sum(k)) < minn and j!=k:
                minn = abs(sum(j) - sum(k))
                finalj = j
                finalk = k
    if values[0] in finalk:
        print(" ".join(str(x) for x in finalk+finalj))
    else:
        print(" ".join(str(x) for x in finalj+finalk))
