def prefix(words):
    first = []
    ans = ""
    for i in range(0, len(words), 2):
        test = words[i:i+2]
        if len(test) == 1:
            first.append(test[0])
        else:
            entry = []
            for i,j in zip(test[0],test[1]):
                if i==j:
                    entry.append(i)
                else:
                    break
            first.append("".join(entry))
    ans = " ".join(str(x) for x in first)
    if len(words) == 1:
        return ''
    else:
        return ans + " " + prefix(first)

N = int(input())
for i in range(N):
    words = input().split(" ")
    print(prefix(words))
