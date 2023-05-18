#gagawa ng dict tapos lilitaw ans

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
            memo[(n,'HARD')] = math.ceil(1.2* math.ceil(I(n-1, 'HARD')))
    return memo[(n,kind)]

cards, new = input().split()
cards = int(cards)
new = int(new)
deck = dict()
days = []
for i in range(cards):
    entry = input()
    if len(entry) <= 6:
        kind = 'GOOD'
    else:
        kind = 'HARD'
    deck[entry] = [kind,0,0] #word:[kind,n (ilang beses nakita),count(In)]
keys = list(deck.keys())
queries = int(input())
for j in range(queries):
    querie = int(input())
    days.append(querie)
goal = max(days)
ans = dict()
for day in range(1,goal+1):
    ans[day] = []
    if day == 1: #establish day 1
        if new > len(keys):
            for x in keys:
                ans[1].append(x)
                deck[x][1] = 1
                deck[x][2] = 1
        else:
            for x in range(new):
                ans[1].append(keys[x])
                deck[keys[x]][1] = 1
                deck[keys[x]][2] = 1
    else:
        if len(keys) > new: #habang keri pa ng laman ni keys, add langz by new
            for x in range(new):
                ans[day].append(keys[x])
                deck[keys[x]][1] = 1
                deck[keys[x]][2] = 1
        else:
            for x in range(len(keys)): #if di na abot sa new, dagdag na lang natira
                ans[day].append(keys[x])
                deck[keys[x]][1] = 1
                deck[keys[x]][2] = 1
        for y in deck:
            if y in ans[day-1]: #if laman ni prev day
                if deck[y][1] == 1 or deck[y][1] == 0: #pag isang beses pa lang nakita, dagdag
                    ans[day].append(y)
                    deck[y][1] = deck[y][1] + 1
                    deck[y][2] = I(deck[y][1],deck[y][0])
            if deck[y][1] !=0 and deck[y][2] == 0: #napakita na pero nareset na
                ans[day].append(y)
                deck[y][1] = deck[y][1] + 1
                deck[y][2] = I(deck[y][1],deck[y][0])
            elif deck[y][1] !=1 and deck[y][2] != 0: #nakita na pero may laman pa
                deck[y][2] = deck[y][2] - 1

    #print(day,deck['ulimwengu'][1],deck['ulimwengu'][2])
    left = [x for x in keys if deck[x][1] == 0 and x not in ans[day]]
    keys = left #update keys, remove yung mga nasa ans para choices na idadagdag
    ans[day].sort()
for querie in days:
    if ans[querie] == []:
        print('NONE')
        print('---')
    else:
        for answer in ans[querie]:
            print(answer)
        print('---')
        
