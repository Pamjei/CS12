#in counter method
N = int(input())
for i in range(N):
    sums = []
    pairs = {}
    start,end = input().split()
    start = int(start)
    end = int(end)
    for i in range(start,end+1):
        total = eval("+".join(str(i)))
        sums.append((total,i))
    for j in sums:
        if j[0] in pairs:
            pairs[j[0]].append(j[1])
            pairs[j[0]][0] = pairs[j[0]][0] + 1
        else:
            pairs[j[0]] = [1,j[1]] #first element in list is count
    print(pairs)
