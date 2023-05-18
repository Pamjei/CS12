def expand(acronym, N):
    return realz(acronym, acronym, N)

def realz(acronym, orig, N):
    if N == 0:
        return acronym
    else:
        words = acronym.split()
        for x in range(len(words)):
            if words[x].isupper():
                words[x] = orig
        words = " ".join(str(x) for x in words)
        return realz(words, orig, N-1)

OTHER_RECURSIVE_FUNCTIONS = ["realz"]

#di gumagana pag n<3
#kada recurse nagbabago pala yung words
