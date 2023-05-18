#puta gumana ka rin
import math
def recurse(members, commissions, principal_money, index, under_you):
    if index >= len(members):
        return 0
    elif under_you == False:
        index = members.index("YOU")
    if members[index] == "YOU":
        under_you = True
    if under_you == True:
        if members[index] == "":
            return 0
        else:
            money = principal_money[index]*commissions[index]*0.5**(math.floor(math.log2(index+1)))
            return money + recurse(members, commissions, principal_money, 2*index+1, under_you) + recurse(members, commissions, principal_money, 2*index+2, under_you)
    #return recurse(members, commissions, principal_money, index+1, under_you)

members = ['Bob', 'Alice', 'YOU', 'Chris', 'Brandon', '', 'Ken']
commissions = [0.1, 0.2, 0.3, 0.2, 0.1, 0.1, 0.21]
principal_money = [500, 100, 1000, 1000, 1000, 1000, 1000, 1000]

result = recurse(members, commissions, principal_money, 0, False)

print(result)
#money = principal_money[index]*commissions[index]*0.5**(math.floor(math.log2(index+1)))

