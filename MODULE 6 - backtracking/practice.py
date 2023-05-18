from collections import Counter

l1 = [12,17,17,14]
l2 = [12,17]
c1 = Counter(l1)
c2 = Counter(l2)

diff = c1-c2
print(set(l1)-set(l2))
