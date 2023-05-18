#code ni pam
N = int(input())
for i in range(N):
    sums = []
    pairs = {}
    counts = {}
    start,end = input().split()
    start = int(start)
    end = int(end)
    for i in range(start,end+1):
        total = eval("+".join(str(i)))
        sums.append((total,i))
    for j in sums:
        if j[0] in pairs:
            pairs[j[0]].append(j[1])
        else:
            pairs[j[0]] = [j[1]]
    for k in pairs:
        if len(pairs[k]) in counts:
            counts[len(pairs[k])].append(pairs[k])
        else:
            counts[len(pairs[k])] = [pairs[k]]
    counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[0], reverse=True)}
    print(next(iter(counts.values())))
