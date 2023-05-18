A = str(input())
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
print(A)
