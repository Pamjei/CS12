n = int(input())
output = []
for i in range(n):
    total = []
    check = 0
    input_string = input()
    rankings = input_string.split(" ")
    rankings = [int(i) for i in rankings]
    length = len(rankings)
    
    for j in range(length-1):
        small = 0
        big = 0
        for TestBig in range(j+1, length):
            if rankings[j] < rankings[TestBig]:
                big = big + 1
        #print('big',big)
        for TestSmall in range(0,j):
            if rankings[j] > rankings[TestSmall]:
                small = small + 1
        #print('small',small)
        total.append(big*small)
    output.append(sum(total))
for i in range(n):
    print(output[i])

#MAG IIBA ATA LAHAT KASI HINDI NA NEED NA MAGKASUNOD REVIEW NA LANG BUKAS SHET

#TLE 7.6s
