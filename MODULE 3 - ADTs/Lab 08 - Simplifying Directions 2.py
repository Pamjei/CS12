N = int(input())
for i in range(N):
    directions = list(input().split())
    pairs = {'RIGHT':'LEFT', 'LEFT':'RIGHT', 'UP':'DOWN', 'DOWN':'UP'}
    stack = []
    for i in directions:
        if stack and pairs[i] == stack[-1]:
            stack.pop()
            print(stack,0)
        else:
            stack.append(i)
            print(stack,1)
    print(" ".join(str(x) for x in stack))
