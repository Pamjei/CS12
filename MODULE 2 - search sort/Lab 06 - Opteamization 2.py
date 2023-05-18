from operator import itemgetter
N = int(input())
Output = [ ]
for i in range(N):
    L = int(input())
    times = [ ]
    remove = [ ]
    for j in range(L):
        time = (input().split())
        time = [int(i) for i in time]
        times.append(time)
    times = sorted(times, key = itemgetter(0,1))
    for x in range(L-1):
        if times[x][1] >= times[x+1][0]:
           remove.append(times[x+1][0])
           if times[x][1] >= times[x+1][1]:
               remove.append(times[x+1][1])
           else:
               remove.append(times[x][1])
    ans = [item for sublist in times for item in sublist] #remove sublist
    final = [i for i in ans if i not in remove] #remove unwanted
    Output.append(sorted(final))   
for i in range(N):
    print(" ".join(str(x) for x in Output[i]))

#remove method
#di gumagana if [1,3],[1,4],[1,6]
