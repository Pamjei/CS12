#TANGINANG SPACE YAN SA SPLIT GRRRR
def prefix(words):
    common = []
    for i in range(0, len(words), 2):
        test = words[i:i+2]
        if len(test) == 1:
            common.append(test[0])
        else:
            entry = []
            for i,j in zip(test[0],test[1]):
                if i==j:
                    entry.append(i)
                else:
                    break
            common.append("".join(entry))
    return common

N = int(input())
for i in range(N):
    words = input().split()
    ans = []
    while len(words) > 1:
        entry = prefix(words)
        ans.append(" ".join(entry))
        words = entry
    print(" ".join(ans))
