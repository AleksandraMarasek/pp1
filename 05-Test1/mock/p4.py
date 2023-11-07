def f(card_number):
    if len(card_number)!=16:
        return False
    else:
        return card_number[:2]+10*'*'+card_number[12:]
    

print(f("5290312400019022"))