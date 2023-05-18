start = str(input())
p1 = set()
p2 = set()
p3 = set()
people = [p1, p2, p3]
if start == "---":
    entry = ""
    for i in people:
        while entry != "---":
            entry = str(input())
            i.add(entry)
        else:
            entry = ""
        i.remove("---")
    unique_p1 = sorted(list(p1 - p2 - p3))
    unique_p2 = sorted(list(p2 - p1 - p3))
    unique_p3 = sorted(list(p3 - p2 - p1))
    common = sorted(list(set.intersection(*people)))
    
for j in unique_p1:
    print(j)
print("---")
for k in unique_p2:
    print(k)
print("---")
for l in unique_p3:
    print(l)
print("---")
for x in common:
    print(x)
