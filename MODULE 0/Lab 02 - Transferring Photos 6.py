n = int(input())
output = []
for i in range(n):
    low = int(input())
    med = int(input())
    goal = int(input())
    for x in range(1,med+1):
        left = goal - (5*x)
        if left < 1:
            break
    if left == 1 and med == 1: #special case na walang kwenta si med
        for y in range(1,low+1):
            left = goal - (2*y)
            if left == 0:
                output.append(y)
                break
        if left > 0:
            output.append(-1)
    elif left == 0:
        output.append(0)
    else:
        if left == -1 or left == -3:
            left = left + 5
        elif left == -2 or left == -4:
            left = left + 10
        elif left%2 != 0 and med > 1:
            left = left + 5
        for y in range(1,low+1):
            LowPics = left - (2*y)
            if LowPics == 0:
                output.append(y)
                break
        if LowPics > 0:
            output.append(-1)
for i in range(len(output)):
    print (int(output[i]))

#find a way pag left = 0
