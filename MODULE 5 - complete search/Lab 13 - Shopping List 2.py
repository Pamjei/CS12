from operator import itemgetter
needs = input().split()
N = int(input())
catalog = {}
for i in range(N):
    shop = str(input())
    total = []
    entry = shop.split(":") #ahop, item price item price
    items = entry[1].split() #item, price, item, price
    for x in range(0,len(items)-1,2):
        if items[x] in needs:
            total.append(int(items[x+1]))
    catalog[entry[0]] = sum(total)
print(catalog)

#okay wow this does not work kasi repetition
