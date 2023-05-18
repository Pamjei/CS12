
N = int(input())
Output = [ ]
for i in range(N):
    L = int(input())
    times = [ ]
    ans = [ ]
    for j in range(L):
        time = list(input().split(" "))
        times.append(time)
    times = sorted(times)
    new_times = sorted(times)
    for x in range(L-1):
        if times[x][1] >= times[x+1][0]:
            ans.append(times[x][0])
            ans.append(times[x+1][1])
            new_times.remove(times[x+1])
            new_times.remove(times[x])
            print(times[x])
    final_times = [item for sublist in new_times for item in sublist]
    combi = (final_times + ans)
    final = sorted([int(k) for k in combi])
    Output.append(final)
for i in range(N):
    print(" ".join(str(x) for x in Output[i]))
