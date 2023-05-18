
N = int(input())
Output = []
for i in range(N):
    titles = list(input().split(","))
    weights = list(input().split())
    rank = int(input())
    scores = []
    if "" in titles:
        Output.append("No books")
    elif rank > len(titles):
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
        for x in range(len(scores)-1):
            if scores.count(sorted_pairs[x][0]) > 1 and sorted_pairs[x][0] == sorted_pairs[x+1][0]:
                if sorted_pairs[x][1] > sorted_pairs[x+1][1]:
                    sorted_pairs[x][1], sorted_pairs[x+1][1] = sorted_pairs[x+1][1], sorted_pairs[x][1]
        print(sorted_pairs)
        #Output.append(sorted_pairs[0][1])
for i in range(N):
    print(Output[i])

#HANAP NG WAY FOR DUPE SCORES
#mali na siya if multiple dupes huhu
