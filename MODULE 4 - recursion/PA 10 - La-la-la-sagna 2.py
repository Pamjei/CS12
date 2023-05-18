def lasagna(N,i):
    cheese, beef,tomato1, tomato2, pepper = '','','','',''
    top_pasta = '~'*(2*N+3) + '\n'
    bottom_pasta = '~'*(2*N+3)
    if i%2 == 0: #i//2 yung layers of tomatos
        for x in range(i//2):
            tomato1 = tomato1 + ('o'*(2*N+3) + '\n')
        for y in range(i//2):
            tomato2 = tomato2 + ('o'*(2*N+3) + '\n')
    else:
        for z in range((i//2)+1):
            tomato1 = tomato1 + ('o'*(2*N+3) + '\n')
        for a in range(i//2):
            tomato2 = tomato2 + ('o'*(2*N+3) + '\n')
    if i%4 == 1:
        beef = '*'*(2*N+3) + '\n'
    if i%4 == 2:
        cheese = '#'*(2*N+3) + '\n'
    if i%4 == 3:
        pepper = '='*(2*N+3) + '\n'
    if i == N:
        return 0
    else:
        return f'{cheese}{top_pasta}{tomato1}{lasagna(N,i+1)}{tomato2}{beef}{bottom_pasta}'
    
N = int(input())
print(lasagna(N,1))

#sa gitna ang recursion? how men
midval = int((len(lasag))/2)
    if i == N:
        return '\n'.join(lasag)
    if midval % 2 == 0:
        inserted = lasag.insert(midval, lasagna(N, i+1))
        return '\n'.join(inserted)
    else:
        inserted = lasag.insert(midval+1, lasagna(N, i+1))
        return '\n'.join(inserted)
