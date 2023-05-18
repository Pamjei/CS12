#USING SINGLE LIST
N = int(input())
Output = []
for i in range(N):
    Row1 = list(input())
    Row2 = list(input())
    Row3 = list(input())
    Array = Row1 + Row2 + Row3
    for i in range(0,5):
        Array[i], Array[i+3] = Array[i+3], Array[i]
        if i < 3: #swapping row 1
            if all(Array[i] == element for element in Array[0:3]) or all(Array[i+3] == element for element in Array[3:6]):
                print('YES')
                break
            else: #swapping row 2
                Array[i], Array[i+3] = Array[i+3], Array[i]
        else:
            if all(Array[i] == element for element in Array[3:6]) or all(Array[i+3] == element for element in Array[6:9]):
                print('YES')
                break
            else:
                Array[i], Array[i+3] = Array[i+3], Array[i]
    for i in range(0,7):
        Array[i], Array[i+1] = Array[i+1], Array[i]
        if : #apply step concept
            if all(Array[i+1] == element for element in Array[0:8:3]) or all(Array[i] == element for element in Array[0:8:3]):
            else:
                Array[i], Array[i+1] = Array[i+1], Array[i]
    
    if Array == Row1 + Row2 + Row3:
        print('NO')
for i in range(N):
    print(Output[i])
