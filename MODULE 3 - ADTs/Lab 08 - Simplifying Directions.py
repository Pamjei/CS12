N = int(input())
for i in range(N):
    directions = list(input().split())
    #pairs = [('RIGHT','LEFT'), ('LEFT','RIGHT'), ('UP','DOWN'), ('DOWN','UP')]
    stak = []
    stak.append(directions[0])
    for direct in directions:
        top = stak[-1]
        #ind = pairs.ind(top)
        if direct == 'LEFT' and top == 'RIGHT':
            stak.pop()
        elif direct == 'RIGHT' and top == 'LEFT':
            stak.pop()
        elif direct == 'UP' and top == 'DOWN':
            stak.pop()
        elif direct == 'DOWN' and top == 'UP':
            stak.pop()
        else:
            stak.append(direct)
    if stak == []:
        print(stak)
    else:
        stak.remove(directions[0])
        print(" ".join(str(x) for x in stak))

#matic na na-aadd yung una kahit na pakshet siya
#IR siguro sa stak[-1] (?)
