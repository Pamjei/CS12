#USING MULTIPLE LISTS
#IT WORKS!!!
N = int(input())
Output = []
for x in range(N):
    Answer = []
    Row1 = list(input())
    Row2 = list(input())
    Row3 = list(input())
    Array = Row1 + Row2 + Row3
    for i in range(0,3):
        Row1[i],Row2[i] = Row2[i],Row1[i]
        if len(set(Row1))== 1 or len(set(Row2))== 1:
            Answer.append('YES')
            break
        else:
            Row1[i],Row2[i] = Row2[i],Row1[i]
    for i in range(0,3):
        Row2[i],Row3[i] = Row3[i],Row2[i]
        if len(set(Row2))== 1 or len(set(Row3))== 1:
            Answer.append('YES')
            break
        else:
            Row2[i],Row3[i] = Row3[i],Row2[i]
    for i in range(0,2):
        Row1[i],Row1[i+1] = Row1[i+1],Row1[i]
        if Row1[i] == Row2[i] == Row3[i] or Row1[i+1] == Row2[i+1] == Row3[i+1]:
            Answer.append('YES')
            break
        else:
            Row1[i],Row1[i+1] = Row1[i+1],Row1[i]
    for i in range(0,2):
        Row2[i],Row2[i+1] = Row2[i+1],Row2[i]
        if Row1[i] == Row2[i] == Row3[i] or Row1[i+1] == Row2[i+1] == Row3[i+1]:
            Answer.append('YES')
            break
        else:
            Row2[i],Row2[i+1] = Row2[i+1],Row2[i]
    for i in range(0,2):
        Row3[i],Row3[i+1] = Row3[i+1],Row3[i]
        if Row1[i] == Row2[i] == Row3[i] or Row1[i+1] == Row2[i+1] == Row3[i+1]:
            Answer.append('YES')
            break
        else:
            Row3[i],Row3[i+1] = Row3[i+1],Row3[i]
    
    if 'YES' in Answer:
        Output.append('YES')
    else:
        Output.append('NO')

for x in range(N):
    print(Output[x])

