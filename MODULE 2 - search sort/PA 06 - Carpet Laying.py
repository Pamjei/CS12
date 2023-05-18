from operator import itemgetter
T = int(input())
for i in range(T):
    N = int(input())
    carpets = []
    overlaps = []
    for j in range(N):
        carps = (input().split())
        carps = [int(i) for i in carps]
        carpets.append(carps)
        carpets = sorted(carpets, key = itemgetter(0,1))
    for x in range(len(carpets)):
        for y in range(x,len(carpets)):
            if carpets[x][1] > carpets[y][1] and carpets[x][1] != carpets[y][0]:
                overlaps.append([carpets[y][0],carpets[y][1]])
            elif carpets[x][1] > carpets[y][0] and carpets[x][1] != carpets[y][0]:
                overlaps.append([carpets[y][0],carpets[x][1]])
    if overlaps != carpets:
        for z in carpets:
            if z in overlaps:
                overlaps.remove(z)
        overlaps.sort()
        ans = [item for sublist in overlaps for item in sublist]
        print(" ".join(str(x) for x in ans))
