def cards_value(card):
    if card in ['A','K','Q','J','T']:
        return 10
    else:
        return int(card)

def f(player1,player2):
    player1_sum=sum(cards_value(card) for card in player1)
    player2_sum=sum(cards_value(card) for card in player2)
    
    return True if player1_sum>=player2_sum else False

print(f("AJ972","AQT72"))

