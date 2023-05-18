import math
def recurse(members, commissions, principal_money, index, under_you):
    money = 0
    if members[index] == "YOU":
        under_you = True
        
    if under_you == True:
        money = principal_money[index]*commissions[index]*0.5**(math.floor(math.log2(index+1)))
    
    if 2*index+1 >= len(members) or members[index] == "":
        return 0
    else:
        return money + recurse(members, commissions, principal_money, (2*index)+1, under_you)

#yung pagkuha na lang shet

members = ['Bob', 'Alice', 'YOU', 'Chris', 'Brandon', 'Ben', 'Ken']
commissions = [0.1, 0.2, 0.3, 0.2, 0.1, 0.1, 0.21]
principal_money = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]

result = recurse(members, commissions, principal_money, 0, False)
print(result)
#money = principal_money[index]*commissions[index]*0.5**(math.floor(math.log2(index+1)))
