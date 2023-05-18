N = int(input())
output = []
for i in range(N):
    m,n = input().split(" ")
    m = int(m)
    n = int(n)
    initial = m
    count = 0
    while m >= n:
        recycled = m - n + 1
        m = recycled
        count = count + 1
    total = count + initial
    output.append(total)
for i in range(N):
    print(output[i])
