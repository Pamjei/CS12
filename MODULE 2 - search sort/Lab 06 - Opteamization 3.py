from operator import itemgetter
N = int(input())
Output = [ ]
for i in range(N):
    L = int(input())
    times = []
    ans = []
    for j in range(L):
        time = (input().split())
        time = [int(i) for i in time]
        times.append(time)
    times = sorted(times, key = itemgetter(0,1))
    for x in range(L-1):
        if times[x][1] >= times[x+1][0]:
           if times[x][1] >= times[x+1][1]:
               ans.append(times[x][1])
               ans.append(times[x][0])
           else:
               ans.append(times[x+1][1])
               ans.append(times[x][0])
        else:
            ans.append(times[x][0])
            ans.append(times[x][1])
    final = set(ans)
    
    Output.append(sorted(final))   
for i in range(N):
    print(" ".join(str(x) for x in Output[i]))

#di gumagana if naulit ganun
#dapat while loop na lang
