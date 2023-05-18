#IT WORKSSSSSS
def expand(acronym, N):
    base = []
    words = acronym.split()
    for i in range(len(words)):
        if words[i].isupper():
            caps = words[i]
            index = i
    if index == len(words)-1:
        [base.append(x) for x in words if x not in base]
    else:
        [base.append(x) for x in words if x not in base or x.isupper()]
        for j in base[::-1]:
            if j == caps:
                base.pop()
            else:
                break
    base = " ".join(str(y) for y in base)
    
    if N == 1:
        return acronym
    return expand(acronym.replace(caps,base),N-1)
