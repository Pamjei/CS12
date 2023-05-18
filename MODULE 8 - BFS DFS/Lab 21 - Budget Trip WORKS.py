#IT WOOORKKSSSSS
import heapq
import math

def dijkstra(G, S):
    pq = []
    costs = {v: math.inf for v in G}
    costs[S] = 0
    heapq.heappush(pq, (0, S))
    while pq:
        d_u, u = heapq.heappop(pq)
        for e in G[u]:
            v, w = e
            d_v = costs[v]
            if d_v > d_u + w:
                costs[v] = d_u + w
                heapq.heappush(pq, (d_u + w, v))
    return costs

gas_money = int(input())
places = input().split()
places.sort()
N = int(input())
G = {'Home':[]}
for i in range(N):
    x,y,z = input().split()
    if x not in G:
        G[x] = [(y, int(z))]
        if y not in G:
            G[y] = [(x, int(z))]
    else:
        G[x].append((y, int(z)))
        if y not in G:
            G[y] = [(x, int(z))]
for a in places:
    if a not in G:
        G[a] = []
ans = []
costs = dijkstra(G, 'Home')
placecost = {x:costs[x] for x in places}
for i in placecost:
    if gas_money > placecost[i]:
        ans.append(i)
if ans == []:
    print('None')
else:
    print(" ".join(ans))
