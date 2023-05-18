N = int(input())
for i in range(N):
    D = int(input())
    G = int(input())
    L = input().split()
    S = int(input())
    E = int(input())
    bought = 0
    for x in range(S-1,E):
        L[x] = 0
    if set(L) == {0}:
        print(-1)
    else:
        L = [int(x) for x in L]
        for days in range(D):
            bought = bought + L[days]
            if bought >= G:
                print(days+1)
                break
        if bought < G:
            print(-1)
        
