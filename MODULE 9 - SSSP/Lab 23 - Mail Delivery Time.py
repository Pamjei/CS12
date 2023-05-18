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

N = int(input())
for i in range(N):
    G = dict()
    nodes = set()
    entry = input().split()
    for i in range(0,len(entry),3):
        if int(entry[i]) not in G:
            G[int(entry[i])] = [(int(entry[i+1]),int(entry[i+2]))]
        else:
            G[int(entry[i])].append((int(entry[i+1]),int(entry[i+2])))
    n = int(input())
    k = int(input())
    ans = []
    for a in range(1,n+1):
        if a not in G:
            G[a] = []
    costs = dijkstra(G, k)
    values = list(costs.values())
    if math.inf in values:
        print(-1)
    else:
        print(max(values))
