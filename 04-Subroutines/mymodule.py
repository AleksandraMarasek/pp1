import random

def generate_number():
    o=random.randint(1,9)
    return o

def month(n):
    month_names=['January','February','March','April','May','June','July','August','September','October','November','December']
    if n>=1 and n<=12:
        return month_names[n-1]
    else:
        return 'Invalid month number'
    
if __name__=="__main__":
    n=int(input('Enter month number: '))
    month_name=month(n)
    print(f'The name of month {n} is {month_name}')

