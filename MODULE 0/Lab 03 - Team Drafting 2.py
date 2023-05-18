n = int(input())
output = []
for i in range(n):
    total = []
    input_string = input()
    rankings = input_string.split(" ")
    rankings = [int(i) for i in rankings]
    length = len(rankings)
        
    for j in range(length-1):
        small = 0
        big = 0
        product = sum(rankings[x] > rankings[j] for x in range(j+1, length)) * sum(rankings[x] < rankings[j] for x in range(0,j))
        total.append(product)
    output.append(sum(total))
    
for i in range(n):
    print(output[i])

#AYUSIN YUNG BIG AND SMOL
#may problema pag hindi arranged ;-;
#https://www.geeksforgeeks.org/python-number-of-values-greater-than-k-in-list/

#TLE 6.5s
