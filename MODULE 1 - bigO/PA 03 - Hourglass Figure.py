
n = int(input())
Output =[]
for j in range(1,n+1):
    i = int(input())
    base = (2*i)+1 #-
    Top_space = 0
    Bottom_space = i+1
    Top_Bottom = 'o' + str('-'*base) + 'o'
    
    Output.append(Top_Bottom)
    for x in reversed(range(1,i+1)):
        Top_in = (x)+(x-1)
        Top_space += 1
        Top_Glass = ' '*Top_space + '\\' + ' '*Top_in + '/'
        print(Top_Glass)
        Output.append(Top_Glass)
    Output.append(' '*(i+1) + 'X')
    for y in (range(1,i+1)):
        Bottom_in = (y)+(y-1)
        Bottom_space -= 1
        Bottom_Glass = ' '*Bottom_space + '/' + '.'*Bottom_in + '\\'
        Output.append(Bottom_Glass)
    Output.append(Top_Bottom)

for i in range(len(Output)):
    print(Output[i]) 
