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

cakeshops = input().split()
N = int(input())
G = {'Home': [], 'Friend': []}
for i in range(N):
    x,y,z = input().split()
    if x == 'Home' and y == 'Friend':
        p = 1
    elif x not in cakeshops and y == 'Friend':
        p = 0
    else:
        if x not in G:
            G[x] = [(y, int(z))]
            if y not in G:
                G[y] = [(x, int(z))]
            else:
                G[y].append((x, int(z)))
        else:
            G[x].append((y, int(z)))
            if y not in G:
                G[y] = [(x, int(z))]
            else:
                G[y].append((x, int(z)))
    for a in cakeshops:
        if a not in G:
            G[a] = []
costs = dijkstra(G, 'Home')
print(costs['Friend'])
