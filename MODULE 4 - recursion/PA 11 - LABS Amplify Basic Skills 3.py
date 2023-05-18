def expand(acronym, N):
    words = acronym.split()
    for x in range(len(words)):
        if words[x].isupper():
            words[x] = acronym
    words = " ".join(str(x) for x in words)
    
    if N == 1:
        return acronym
    return expand(words, N-1)

#di gumagana pag n<3
