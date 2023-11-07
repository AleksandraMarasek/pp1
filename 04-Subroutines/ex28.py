def f(amount_to_pay):
    if amount_to_pay%5 == 0 :
        return amount_to_pay/5
    elif amount_to_pay%5 == 1 :
        return amount_to_pay//5 + 1
    elif amount_to_pay%5 == 2 :
        return amount_to_pay//5 + 1
    elif amount_to_pay%5 == 3 :
        return amount_to_pay//5 + 2
    elif amount_to_pay%5 == 4 :
        return amount_to_pay//5 + 2

    
pln=int(input('Enter amount that needs to be paid (in PLN): '))

result = f(pln)

print(f'Min. number of coins that can be used to pay for the product: {result}')