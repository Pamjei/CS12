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
    elif ord(Name1[0])+1 == ord(Name2[0]) and len(Name2)!=1: #magkasunod tapos mahaba pa si N2
        New_name = Name2[0]
    else:
        for x,letter in enumerate(Name1): #check if same letters si 1 at 2
            if letter != Name2[x]: #if hindi same letter
                if ord(letter)+1 == ord(Name2[x]):#Magkasunod
                    if x == len(Name2)-1: #same length na kay N2 (COURTNEY COURTNF = COURTNEZ
                        if len(Name1) == len(Name2):
                            New_name = New_name + letter + 'A'
                        else:
                            New_name = New_name + letter + chr(ord(Name1[x+1])+1)
                        break
                    else:
                        New_name = New_name + Name2[x] #AAAAAABB AAABAA = AAAB
                        break
                elif letter < Name2[x]:
                    New_name = New_name + chr(ord(letter)+1)
                    break
            else:
                New_name = New_name + letter
        if '[' in New_name: #this means nagstop sa Z
            New_name = New_name[:-1]
            for y in range(x+1,len(Name1)):
                if Name1[y] == 'Z': #add lang ng Z
                    New_name = New_name + Name1[y]
                else: #ord(Name1[y])+1 == Name2[x]: #if yung natira kay N2 ay kasunod ni N1
                    New_name = New_name + chr(ord(Name1[y])+1) #yung susunod kay N1
                    break
            if New_name == Name1:
                    New_name = New_name + 'A'
    print(New_name)
#check mo sa bawat letter if nasa name1, if not, hanapin yung smallest in between
#DAPAT ARRANGE MUNA BY LEN THEN BY ALPHABETICAL? NO
#DAPAT NASA GITNA NILA LIKE NG NAMES MISMO COURTNEY < COURTNEZ < COURTNFY
#PUTA ANONG MALI TC3&4 AYAW POTA
