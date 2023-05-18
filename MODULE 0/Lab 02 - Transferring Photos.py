n = int(input())
output = []
for i in range(n):
    low = int(input())
    med = int(input())
    goal = int(input())
    if goal-(med*5) > 1: #check if mauuna si med
        left = (goal-(med*5))
        x = int(left/2)
        print(x)
        if x <= low:
            output.append(x)
        else:
            output.append(-1)
    elif goal -(med*5) == 0:
        output.append(0)
    else:
        x  = goal/2
        if x == 0:
            output.append(x)
        else:
            output.append(-1)
for i in range(n):
    print (int(output[i]))
