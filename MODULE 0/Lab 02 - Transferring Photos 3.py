n = int(input())
output = []
for i in range(n):
    low = int(input())
    med = int(input())
    goal = int(input())
    count = 0
    if goal-(med*5) == 1: #check if hindi need si med
        x  = goal/2
        if x <= low:
            output.append(x)
        else:
            output.append(-1)
    elif goal-(med*5) == 0: #check if hindi need si low
        output.append(0)
    elif goal-(med*5) < 1: #check if sobra medpics
        MedPics = goal//5
        left = goal - (MedPics*5)
        while left%2 != 0:
            left = left + 5
            if left < 0:
                output.append(-1)
                break
        else:
            output.append(left/2)
    else: #if kulang medpics
        left = goal-(med*5)
        if med > 1:
            while left%2 != 0:
                left = left + 5
            else:
                output.append(left/2)
        else:
            if left%2 == 0:
                output.append(left/2)
            else:
                output.append(-1)
for i in range(len(output)):
    print (int(output[i]))

#di ko na alam mama
