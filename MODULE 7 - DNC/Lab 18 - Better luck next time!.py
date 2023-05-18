#omg thank u bisect
import bisect
N = int(input())
for i in range(N):
    scores = input().split()
    goal = input().split()
    sums = []
    ans = []
    for i in range(0,len(scores),3):
        total = int(scores[i]) + int(scores[i+1]) + int(scores[i+2])
        sums.append(total)
    goal = [int(i)*3 for i in goal]
    for j in goal:
        ans.append(bisect.bisect_left(sums,j))
    print(' '.join(str(x) for x in ans))
