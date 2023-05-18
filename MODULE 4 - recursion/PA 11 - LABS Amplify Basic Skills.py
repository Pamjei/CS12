def expand(acronym, N):
    li = acronym.split()
    for word in li:
        if word.isupper():
            caps = word
    li.remove(caps)
    ans = " ".join(str(x) for x in li)
    
    if N == 0:
        return ""
    return f'{ans} {expand(acronym, N-1)}'

#di ko pa alam pano caps
