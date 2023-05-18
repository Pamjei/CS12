#malapit na e, kailangan lang i-limit yung pag add ng children
def BFS(G, v):
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

children = BFS(G,'Home')
ans = []
for i in children:
    if i in places:
        ans.append(i)
if ans == []:
    print('None')
else:
    print(" ".join(sorted(ans)))
