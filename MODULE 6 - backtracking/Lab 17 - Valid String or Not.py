def validator(entry):
    stack = []
    check = ''.join(x for x in entry if not x.isalpha())
    for paren in check:
        if paren == "(":
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            top = stack[-1]
            match = (top == "(" and paren == ")")
            if not match:
                break
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
                
N = int(input())
for i in range(N):
    entry = list(input())
    ans = []
    if validator(entry):
        print(''.join(x for x in entry))
    else:
        for x in range(len(entry)):
            test = entry[:x] + entry[x+1:]
            if validator(test):
                answer = ''.join(x for x in test)
                if answer not in ans:
                    ans.append(answer)
        if len(ans) == 0:
            print(False)
        else:
            print(" ".join(y for y in ans))
