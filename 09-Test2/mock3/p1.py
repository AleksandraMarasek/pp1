def f(player1,player2):
    sum1=0
    sum2=0
    for card in player1:
        try:
            sum1+=int(card)
        except ValueError:
            sum1+=10
    for card in player2:
        try:
            sum2+=int(card)
        except ValueError:
            sum2+=10

    if sum1>=sum2:
        return True
    else:
        return False
    
print(f("AJ972","AQT")  )
