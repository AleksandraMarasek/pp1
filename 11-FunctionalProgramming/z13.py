'''13.	In a beverage factory, a machine fills bottles of various capacities. 
A computer checks whether a bottle has been filled correctly. 
The allowable tolerance is 2% for a 500ml bottle, 3% for a 1000ml bottle and 5% for a 1500ml bottle. 
Write a program that checks whether the bottle has been filled correctly or not. 
Define a higher order function.'''


def bottle_size(size):
    def correctly_filled(filled):
        if size==500:
            if filled>=size-(size*0.02) and filled<=size+(size*0.02):
                return True
        if size==1000:
            if filled>=size-(size*0.03) and filled<=size+(size*0.03):
                return True
        if size==1500:
            if filled>=size-(size*0.05) and filled<=size+(size*0.05):
                return True
        else:
            return False
            
    return correctly_filled

assess_tes500=bottle_size(500)
assess_tes1000=bottle_size(1000)
assess_tes1500=bottle_size(1500)

print(f"507: {assess_tes500(507)}")
print(f"489: {assess_tes500(489)}")
print(f"984: {assess_tes1000(984)}")
print(f"1032: {assess_tes1000(1032)}")
print(f"1578: {assess_tes1500(1578)}")
print(f"1430: {assess_tes1500(1430)}")