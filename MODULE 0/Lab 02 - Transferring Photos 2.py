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
    elif goal-(med*5) == 0:
        output.append(0)
    else:
        for j in range(med):
            left = goal - (j*5)
            if left > goal:
                print(left)
                break
        for k in range(low):
            left = left - 2
            count = count + 1
            if left == 0:
                output.append(count)
                break
        if left > 0:
            output.append(-1)
for i in range(len(output)):
    print (int(output[i]))
