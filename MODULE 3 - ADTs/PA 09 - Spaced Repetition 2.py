#using I(n) kung kelan lilitaw
#NO THIS IS FAIL
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
            memo[(n,'GOOD')] = I(n-2,'GOOD') + round(2* I(n-1, 'GOOD'))
        if kind == 'HARD':
            memo[(n,'HARD')] = I(n-2,'HARD') + math.ceil(1.2* I(n-1, 'HARD'))
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
    deck[entry] = [kind,0,'temp'] #word:[kind,n(seen),I(n)next viewing]
keys = list(deck.keys()) #pag nasa ans, tanggal sa keys. ibabalik lang pag tinanggal sa ans
queries = int(input())
for j in range(queries):
    querie = int(input())
    days.append(querie)
goal = max(days)
ans = dict()
for day in range(1,goal+1):
    ans[day] = []
    if day == 1: #day 1 kasi established na yan matic dagdag lahat
        for x in range(new):
            ans[1].append(keys[x])
            deck[keys[x]][1] = 1
            deck[keys[x]][2] = 1
    else:
        ans[day] = ans[day-1] #kunin yung sa prev day
        if len(keys) > 3: #habang keri pa ng laman ni keys, add langz
            for x in range(new):
                ans[day].append(keys[x])
        else:
            ans[day].extend(keys)
        for y in ans[day-1]:
            if deck[y][1] != 1 and deck[y][2] != day:
                deck[y][1] = deck[y][1] + 1
                #deck[y][2] = memo[(deck[y]
                ans[day].remove(y)
    ans[day].sort()
    left = [x for x in keys if x not in ans[day]]
    keys = left
        #sa mga nasa prev day, if ang n nila ay not zero, add 1 sa n tapos remove
        #check deck if may day = I(n) o kaya n = 0 tapos add
print(keys)          
for querie in days:
    print(ans[querie])
        
