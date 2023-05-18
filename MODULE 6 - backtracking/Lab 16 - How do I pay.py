#thank u jed
def generate_payment_terms(all_denominations, money_left, payment_terms):
    count = 0
    if money_left == 0:
        print(payment_terms)
        count = count + 1
        return count
    denoms = [i for i in all_denominations if i <= money_left]
    for i in denoms:
        if money_left >= i and len(payment_terms) <10:
            payment_terms.append(i)
            count = count + generate_payment_terms(all_denominations, money_left-i, payment_terms)
            payment_terms.pop()
    return count
                

all_denominations = [1,5,10,20]
#print(generate_payment_terms(all_denominations, 7, [])) #== 1
print(generate_payment_terms(all_denominations, 10, [])) #== 9
#print(generate_payment_terms(all_denominations, 20, [])) #== 104
#print(generate_payment_terms(all_denominations, 19, [])) #== 75
#print(generate_payment_terms(all_denominations, 29, [])) #== 551
