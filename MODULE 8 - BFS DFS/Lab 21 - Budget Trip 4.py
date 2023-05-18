#malapit na e, kailangan lang i-limit yung pag add ng children
ordering = []
visited = set([])
def toposort(G):
    for v in G:
        if v not in ordering:
            dfs_visit(G, v)
            
def dfs_visit(G, S):
    stak = [S]
    visited.add(S)
    while len(stak) > 0:
        curr = stak[-1]
        for v in G[curr]:
            if v not in visited:
                visited.add(v)
                stak.append(v)
                break
        if curr == stak[-1]:
            ordering.append(curr) # add processed vertex to ordering
            stak.pop()
# toposort result is ordering.reverse()

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
ans = []
toposort(G)
print(ordering)
if ans == []:
    print('None')
else:
    print(" ".join(sorted(ans)))

