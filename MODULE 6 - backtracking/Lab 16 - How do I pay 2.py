def generate_payment_terms(all_denominations, money_left, payment_terms):
    if money_left == 0:
        return 
    
    denoms = [i for i in all_denominations if i <= money_left]
    for i in denoms:
        count = 0
        if money_left >= i:
            payment_terms.append(i)
            if sum(payment_terms) == money_left:
                count = count +1
            return generate_payment_terms(all_denominations, money_left-1, payment_terms)
            payment_terms.pop()
    
all_denominations = [100, 50, 20, 10, 5, 1]
print(generate_payment_terms(all_denominations, 10, [])) #== 1
#print(generate_payment_terms(all_denominations, 10, [])) #== 9
#print(generate_payment_terms(all_denominations, 20, [])) #== 104
#print(generate_payment_terms(all_denominations, 19, [])) #== 75
#print(generate_payment_terms(all_denominations, 29, [])) #== 551
