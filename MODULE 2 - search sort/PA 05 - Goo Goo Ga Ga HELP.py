def get_name(lb,ub):
    res = ""
    for i in range(len(lb)):
        for a in range(ord('A'),ord('Z')+1):
            if lb < res + chr(a) < ub:
                return res + chr(a)
        res += lb[i]
    return res + 'A'
