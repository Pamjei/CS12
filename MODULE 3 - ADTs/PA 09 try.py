import math
memo = dict()
def I(n,kind):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    if (n,kind) in memo:
        return memo[(n,kind)]
    else:
        if kind == 'GOOD':
            memo[(n,'GOOD')] = round(2* I(n-1, 'GOOD'))
        if kind == 'HARD':
            memo[(n,'HARD')] = math.ceil(1.2* I(n-1, 'HARD'))
    return memo[(n,kind)]

print(I(2,'HARD'))
