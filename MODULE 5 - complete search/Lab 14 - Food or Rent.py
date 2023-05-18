import math
N = int(input())
for i in range(N):
    Happiness = {}
    P,c,max_diff,a,m,n = input().split()
    x,y = int(P),int(P)
    c = int(c)
    max_diff = int(max_diff)
    a = float(a)
    m = int(m)
    n = int(n)
    while abs(x-y) <= max_diff and x >=0 and y >=0:
        H = math.sin(a*(x**m) + (1-a)*(y**n))
        Happiness[H] = (x,y)
        x,y = x+c, y-c
    Happiness = {k: v for k, v in sorted(Happiness.items(), reverse=True, key=lambda item: item[0])}
    answer = list(Happiness.values())[0]
    print(answer[0], answer[1])
