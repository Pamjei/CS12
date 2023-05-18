N = int(input())
for i in range(N):
    l = int(input())
    stack = [1]
    x = 0
    for i in range(l):
        entry = str(input())
        if "for" in entry:
            word, n = entry.split()
            n = int(n)
            stack.append(stack[-1]*n)
        elif entry == "end":
            stack.pop()
        elif entry == "add":
            x = x + stack[-1]
    if x < 1000:
        print(x)
    else:
        print('ERROR')
    
#THANK U JOTAN WTH
