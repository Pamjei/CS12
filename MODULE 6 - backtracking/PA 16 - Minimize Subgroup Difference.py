from itertools import combinations
import math

def quad(x,tup): #computes value of f(x)
    a,b,c = tup
    ans = a*(x**2) + b*x + c
    return ans

N = int(input())
for i in range(N):
    quadfunc = dict()
    entry = input().split()
    for i in range(0,len(entry),3):
        quadfunc[(int(entry[i]),int(entry[i+1]),int(entry[i+2]))] = 0
    x = int(input())
    for tup in quadfunc:
        quadfunc[tup] = quad(x,tup)
    values = list(quadfunc.values()) #values of f(x)
    partition = len(values)//2 #how many elements in each tup
    combi = set(combinations(values,partition)) #combi of tup
    ans = dict()
    minn = math.inf
    if len(set(values)) == len(values):
        for j in combi:
            for k in combi:
                diff = abs(sum(j) - sum(k))
                if diff < minn and all(x not in j for x in k):
                    minn = diff
                    ans[minn] = [j,k]
    else:
        for j in combi:
            for k in combi:
                diff = abs(sum(j) - sum(k))
                if diff < minn and j!=k:
                    minn = diff
                    ans[minn] = [j,k]
    ans = {k: v for k, v in sorted(ans.items(), key=lambda item: item[0])}
    final = next(iter(ans.values()))
    if values[0] in final[1]:
        finalfinal = [final[1],final[0]]
        print(" ".join(str(x) for x in list(sum(finalfinal, ()))))
    else:
        print(" ".join(str(x) for x in list(sum(final, ()))))
