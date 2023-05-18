#GUMAGANA NAAAAA
N = int(input())
for i in range(N):
    x = str(input())
    if x == "" or x == " ":
        print(True)
    elif all(char in ['#','*'," "] for char in x):
        print(True)
    else:
        if " " not in x or x[-1]== " ":
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
                    if A.index(char) == 0:
                        A = A.replace(char, "",1)
                    else:
                        A = A.replace(char,A[A.find(next(filter(str.isalnum, A)))],1)
                elif char == "#":
                    if A.index(char) == 0:
                        A = A.replace(char, "",1)
                    else:
                        A = A.replace(char, "",1)
                        A = A.replace(A[A.find(next(filter(str.isalnum, A)))],"",1)
            
        if "*" in B or "#" in B:
            for char in B:
                if char == "*":
                    if B.index(char) == 0:
                        B = B.replace(char, "",1)
                    else:
                        B = B.replace(char,B[B.find(next(filter(str.isalnum, B)))],1)
                elif char == "#":
                    if B.index(char) == 0:
                        B = B.replace(char, "",1)
                    else:
                        B = B.replace(char, "",1)
                        B = B.replace(B[B.find(next(filter(str.isalnum, B)))],"",1)

        if A == B:
            print(True)
        else:
            print(False)
