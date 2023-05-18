from itertools import combinations
import math

N = int(input())
for i in range(N):
    quadfunc = dict()
    entry = input().split()
    x = int(input())
    values = []
    if len(entry)%6 == 0:
        num = len(entry)
    elif len(entry)%3 == 0 and len(entry)%2 != 0:
        num = len(entry[:-3])
    for i in range(0,len(entry),3):
        a,b,c = int(entry[i]),int(entry[i+1]),int(entry[i+2])
        if (a,b,c) not in quadfunc:
            quadfunc[(a,b,c)] = a*(x**2) + b*x + c
        values.append(a*(x**2) + b*x + c)
    partition = len(values)//2 #how many elements in each tup
    ans = dict()
    minn = math.inf
    for j, k in list(set(combinations(list(set(combinations(values,partition))),2))):
        diff = abs(sum(j) - sum(k))
        if len(set(values)) == len(values):
            if diff < minn and all(x not in j for x in k):
                minn = diff
                ans[minn] = [j,k]
        else:
            if diff < minn and j!=k:
                minn = diff
                ans[minn] = [j,k]
    final = ans[min(ans.keys())]
    if values[0] in final[1]:
        finalfinal = final[1]+final[0]
        print(" ".join(str(x) for x in finalfinal))
    else:
        print(" ".join(str(x) for x in list(sum(final, ()))))
