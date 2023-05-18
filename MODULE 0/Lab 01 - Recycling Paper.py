m = int(input())
n = int(input())
    #for i in range(n):
output = []
left = m
while left//n > 0:
    recycled = left//n
    output.append(recycled)
    left = left - recycled
    print(left)
print(output)
total = sum(output) + m
print (total)
 
