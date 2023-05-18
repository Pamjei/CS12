#ITO YUNG GUMAGANA
from operator import itemgetter
N = int(input())
Output = [ ]
for i in range(N):
    L = int(input())
    times = []
    merged = []
    for j in range(L):
        time = (input().split())
        time = [int(i) for i in time]
        times.append(time)
        times = sorted(times, key = itemgetter(0,1))
    for higher in times:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)
            else:
                merged.append(higher)
    final = [item for sublist in merged for item in sublist]
    Output.append(final)  
for i in range(N):
    print(" ".join(str(x) for x in Output[i]))
