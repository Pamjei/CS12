#IT WOOOORKS YEAH
from operator import itemgetter
needs = input().split()
N = int(input())
catalog = {}
for i in range(N):
    shop = str(input())
    entry = shop.split(":")
    items = entry[1].split()
    item_pairs = []
    total = []
    if set(needs).issubset(items): #check if yung needs nandito
        for x in range(0,len(items)-1,2):
            item_pairs.append((items[x],int(items[x+1])))
        item_pairs.sort(reverse=True,key=itemgetter(1))
        item_pairs = dict(item_pairs)
        for y in item_pairs:
            if y in needs:
                total.append(item_pairs[y])
        catalog[entry[0]] = sum(total)
catalog = {k: v for k, v in sorted(catalog.items(), key=lambda item: item[1])}
answer = list(catalog.items())[:1]
print(answer[0][0], answer[0][1])
