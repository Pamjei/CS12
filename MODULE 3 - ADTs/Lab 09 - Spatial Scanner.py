#di ko pa sure pano yung #delete
N = int(input())
for i in range(N):
    SA = ""
    SB = ""
    x = str(input())
    if x == "" or x == " ":
        print(True)
    elif all(char in ['#','*'," "] for char in x):
        print(True)
    else:
        if " " not in x:
            A = x
            B = ""
        elif x[0] == " ":
            A = ""
            B = x
        else:
            A,B = x.split()
            
        if "*" in A or "#" in A:
            for char in A:
                if char == "*":
                    SA = f'{SA}{A[0]}'
                elif char == "#":
                    SA = f'{SA[1:]}'
                else:
                    SA = f'{SA}{char}'
        else:
            SA = A
            
        if "*" in B or "#" in B:
            for char in B:
                if char == "*":
                    SB = f'{SB}{B[0]}'
                elif char == "#":
                    SB = f'{SB[1:]}'
                else:
                    SB = f'{SB}{char}'
        else:
            SB = B
        if "#" in SA or "*" in SA:
            SA = SA.replace("#", "")
            SA = SA.replace("*", "")
        if "#" in SB or "*" in SB:
            SB = SB.replace("#", "")
            SB = SB.replace("*", "")
        #print(SA,SB)

        if SA == SB:
            print(True)
        else:
            print(False)
