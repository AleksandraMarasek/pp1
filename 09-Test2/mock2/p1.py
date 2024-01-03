'''The playing cards have the following values: 
Ace (A), King (K), Queen (Q), Jack (J) and 10 (T) have a value of 
10 each. The other cards have the value indicated by the card number. 
Create a function f(player1,player2) that returns true if the first 
player has cards of the same or higher value, and false otherwise.'''


def f(player1,player2):
    
    sum1=0
    sum2=0
    for i in player1:
        try: 
            x=int(i)
            sum1+=x
        except ValueError:
            sum1+=10

    for i in player2:
        try: 
            x=int(i)
            sum2+=x
        except ValueError:
            sum2+=10
    
    if sum1>=sum2:
        return True
    else:
        return False
    


print(f("AJ972","AQT72"))  

print(f("9532","K8") )
    