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
        sorted_pairs = sorted(paired, key=itemgetter(-0,1))
        print(sorted_pairs)
for i in range(N):
    print(Output[i])

#imbis na i-reverse, - na lang
#di ko pa alam pano
