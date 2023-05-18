from operator import itemgetter
N = int(input())
Output = []
for i in range(N):
    titles = list(input().split(","))
    weights = list(input().split())
    ranks = int(input())
    scores = []
    ind = []
    if "" in titles:
        Output.append("No books")
    elif ranks > len(titles):
        Output.append("Not enough books")
    else:
        weights = [int(j) for j in weights] 
        for x in range(len(titles)):
            rank = 0
            for char in titles[x]:
                num = ord(char) - 96
                rank = rank + num
            total = (rank + len(titles[x]))*weights[x]
            scores.append(total)
        paired = [list(a) for a in zip(scores,titles)]
        sorted_pairs = sorted(paired, reverse=True)
        if any(scores.count(sorted_pairs[element][0]) > 1 for element in range(len(scores))):
            for x in range(len(scores)):
                if scores.count(sorted_pairs[x][0]) > 1:
                    ind.append(x)
            start = min(ind)
            end = max(ind)
            sorted_pairs[start:end+1] = sorted(sorted_pairs[start:end+1], key = itemgetter(1))
        Output.append(sorted_pairs[ranks-1][1])
for i in range(N):
    print(Output[i])

#HANAP NG WAY FOR DUPE SCORES
#isolate yung mga same 
