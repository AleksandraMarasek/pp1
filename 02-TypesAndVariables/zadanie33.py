number=input('Enter your phone number: ')
if len(number)!=9 or not number.isdigit():
    print('invalid phone number')
else:
    number2=(number[:3] +' '+ number[3:6] +' '+ number[6:9])


print('Phone number:',number2)