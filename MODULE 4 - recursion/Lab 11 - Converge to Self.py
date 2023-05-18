def kaprekar(li):
    return counter(li, 1)

def counter(li, i):
    n = list(str(li))
    while len(n) < 4:
        n.append("0")
    n1_list = sorted(n, reverse=True)
    n2_list = sorted(n)
    n1 = int("".join(n1_list))
    n2 = int("".join(n2_list))
    diff = n1 - n2
    if diff == li:
        return i
    elif diff == 0:
        return -1
    else:
        return counter(diff, i+1)

OTHER_HELPER_FUNCTIONS = ['counter']
    
