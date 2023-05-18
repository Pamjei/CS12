#malapit na e, kailangan lang i-limit yung pag add ng children

from collections import deque
pred = {}
def bfs(G, S):
    kyu = deque([S])
    pred[S] = None
    level[S] = 0
    while len(kyu) > 0:
        curr = kyu.popleft()
        neighbors = G[curr]
        for neighbor in neighbors:
            if neighbor not in pred:
                pred[neighbor] = curr
                level[neighbor] = level[curr] + 1  # added
                kyu.append(neighbor)
def child(G, v):
    children = set()
    visited = {key:False for key in G}
    queue = []
    queue.append(v)
    visited[v] = True
    while queue:
        v = queue.pop(0)
        children.add(v)
        for i in G[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return children

gas_money = int(input())
places = input().split()
places.sort()
N = int(input())
G = {'Home':[]}
for i in range(N):
    x,y,z = input().split()
    cost = int(z)
    if x not in G:
        G[x] = [y]
        if y not in G:
            G[y] = [x]
        else:
            G[y].append(x)
    else:
        G[x].append(y)
        if y not in G:
            G[y] = [x]
        else:
            G[y].append(x)
for a in places:
    if a not in G:
        G[a] = []
level = {}
bfs(G,'Home')
children = child(G,'Home')
ans = []
for k,v in level.items():
    if v >=1 and k in children and k in places:
        if gas_money > cost:
            gas_money = gas_money - cost
            ans.append(i)
if ans == []:
    print('None')
else:
    print(" ".join(sorted(ans)))

