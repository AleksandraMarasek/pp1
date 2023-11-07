def f(card_number):
    x=card_number[:2]
    y=card_number[12:]
    result=x+('*'*10)+y
    if len(card_number)==16:
        return result
    else:
        return 'Invalid card number length'