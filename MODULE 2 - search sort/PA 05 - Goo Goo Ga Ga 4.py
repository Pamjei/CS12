T = int(input())
for i in range(T):
    N = int(input())
    Names = []
    New_name = ""
    for j in range(N):
        a = str(input())  
        Names.append(a)
    check = 0
    Names.sort()
    Name1 = Names[(N//2)-1]
    Name2 = Names[N//2]
    if Name1 == Name2[:len(Name1)]: #FRED FREDDIE = FREDA
        New_name = Name1 + 'A'
    elif ord(Name1[0])+1 == ord(Name2[0]) and len(Name2)!=1:
        New_name = Name2[0]
    else:
        for x,letter in enumerate(Name1): #check if same letters si 1 at 2
            if letter == Name2[x]: #if same letters, yun din
                New_name = New_name + letter
            elif ord(letter)+1 == ord(Name2[x]) and len(Name1)>len(Name2): #Magkasunod na letter tapos mas malaki N1
                #if Name1[x+1] == chr(ord(Name2[x])-1):
                    #New_name = New_name + Name2[x] #AAAAAABBA AAABAA = AAAB
                    #break
                if Name1[x+1] == 'Z': #nadadagdag yung susunod pero nagbbreak kay Z
                    New_name = New_name + letter
                    check = 1
                    break
                else:
                    New_name = New_name + letter + chr(ord(Name1[x+1])+1) #COURTNEY COURTNF = COURTNEZ
                    break
            else:
                num = ord(letter) + 1
                New_name = New_name + chr(num)
                break
        if check ==1:
            for y in range(x,len(Name1)):
                if Name1[y] == 'Z':
                    New_name = New_name + Name1[y]
                elif Name1[y] == Name2[x]:
                    New_name = New_name + chr(ord(Name2[x]) + 1)
            if Name1[y] < Name2[x]:
                New_name = New_name + chr(ord(Name1[y]) + 1)
            if New_name == Name1:
                    New_name = New_name + 'A'
    print(New_name)
#check mo sa bawat letter if nasa name1, if not, hanapin yung smallest in between
#DAPAT ARRANGE MUNA BY LEN THEN BY ALPHABETICAL? NO
#DAPAT NASA GITNA NILA LIKE NG NAMES MISMO COURTNEY < COURTNEZ < COURTNFY
#PUTA ANONG MALI TC3&4 AYAW POTA
