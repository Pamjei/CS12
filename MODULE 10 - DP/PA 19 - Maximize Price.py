def maxprice(p,n):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]

    max_choice = maxprice(p, n-1)
    for i in range(1,n+1):
        max_choice = max(max_choice, p[i] + maxprice(p,n-i))
    memo[n] = max_choice
    return max_choice

N = int(input())
for i in range(N):
    entry = input().split()
    p = {entry.index(x):int(x) for x in entry}
    n = int(input())
    memo = dict()
    print(maxprice(p,n))
