def BFS(graph, v):
    children = set()
    visited = {key:False for key in graph}
    queue = []
    queue.append(v)
    visited[v] = True
    while queue:
        v = queue.pop(0)
        children.add(v)
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return children

T = int(input())
for i in range(T):
    graph = dict()
    ans = set()
    N,M,P = input().split()
    for j in range(int(M)):
        x,y = input().split()
        if int(x) not in graph:
            graph[int(x)] = [int(y)]
        else:
            graph[int(x)].append(int(y))
    for a in range(1,int(N)+1):
        if a not in graph:
            graph[a] = [a]
    for k in range(int(P)):
        z = int(input())
        for b in BFS(graph,z):
            ans.add(b)
    print(len(ans))
