
N = int(input())
Output = []
for i in range(N):
    titles = list(input().split(","))
    weights = list(input().split())
    rank = int(input())
    scores = []
    if " " in titles:
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
        zipped_lists = zip(scores, titles)
        sorted_pairs = sorted(zipped_lists, reverse = True)
        
        tuples = zip(*sorted_pairs)
        scores, titles = [ list(tuple) for tuple in tuples]
        set_scores = set(scores)
        #for j in scores:
        #    if scores.count(j)>1:
                
                 
for i in range(N):
    print(Output[i])

#HANAP NG WAY FOR DUPE SCORES
