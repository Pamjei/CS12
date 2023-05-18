T = int(input())
output = []
for i in range(T):
    N = int(input())
    Names = []
    New_name = ""
    for j in range(N):
        a = str(input())  
        Names.append(a)
    Names.sort()
    Name1 = Names[(N//2)-1]
    Name2 = Names[N//2]
    for x,letter in enumerate(Name1): #check if same letters si 1 at 2
        if letter == Name2[x]:
            New_name = New_name + letter
        else:
            num = ord(letter) + 1 #pag wala si 
            New_name = New_name + chr(num)
            break
    print(New_name)
#for i in range(T):
#    print(output[i])

#check mo sa bawat letter if nasa name1, if not, hanapin yung smallest in between
#possible tle: use splicing
