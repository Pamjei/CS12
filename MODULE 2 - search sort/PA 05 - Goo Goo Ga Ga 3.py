T = int(input())
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
    if Name1 == Name2[:len(Name1)]: #FRED FREDDIE = FREDA
        New_name = Name1 + 'A'
    elif 'Z' in Name1 or 'Z' in Name2:
        for x,letter in enumerate(Name1):
            if letter == Name2[x]: #if same letters, yun din
                New_name = New_name + letter
                continue
            elif ord(letter)+1 == ord(Name2[x]) and Name1[x+1]=='Z': #N1 at N2 magkasunod tapos Z yung next ni N1
                if letter == 'Y':
                    New_name = New_name + 'Z'
                    break
                else:
                    New_name = New_name + letter + Name1[x+1]
            elif letter == 'Z':
                New_name = New_name + letter
                if Name1[x+1] == Name2[x]:
                    New_name = New_name + letter + chr(ord(Name1[x+1])+1)
                    break
    else:
        for x,letter in enumerate(Name1): #check if same letters si 1 at 2
            if letter == Name2[x]: #if same letters, yun din
                New_name = New_name + letter
            elif ord(letter)+1 == ord(Name2[x]) and len(Name1)>len(Name2): #Magkasunod na letter tapos mas malaki N1
                if Name1[x+1] == Name2[x]:
                    New_name = New_name + Name2[x] #AAAAAABBA AAABAA = AAAB
                else:
                    New_name = New_name + letter + chr(ord(Name1[x+1])+1) #COURTNEY COURTNF = COURTNEZ 
                break
            else:
                num = ord(letter) + 1
                New_name = New_name + chr(num)
                break
    print(New_name)
#check mo sa bawat letter if nasa name1, if not, hanapin yung smallest in between
#DAPAT ARRANGE MUNA BY LEN THEN BY ALPHABETICAL? NO
#DAPAT NASA GITNA NILA LIKE NG NAMES MISMO COURTNEY < COURTNEZ < COURTNFY
#need to fix pag z yung next; nag index error siya smh
