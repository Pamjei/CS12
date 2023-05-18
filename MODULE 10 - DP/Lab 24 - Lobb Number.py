def binomial(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if (n,k) in memo:
        return memo[(n,k)]
    else:
        memo[(n,k)] = binomial(n-1, k-1) + binomial(n-1, k)
    return memo[(n,k)]

N = int(input())
for i in range(N):
    memo = dict()
    n,m = input().split()
    n = int(n)
    m = int(m)
    memo = dict()
    lobb = ((2*m)+1) * binomial(2*n, m+n) // (m+n+1)
    print(lobb)
