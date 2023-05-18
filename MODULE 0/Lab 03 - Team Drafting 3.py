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
        product = sum(element > rankings[j] for element in rankings[j+1:]) * sum(element < rankings[j] for element in rankings[:j])
        total.append(product)
    output.append(sum(total))
    
for i in range(n):
    print(output[i])

#ITO YUNG GUMAGANA
