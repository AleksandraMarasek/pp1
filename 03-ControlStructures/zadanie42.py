code='0805'

enter=input('Enter the pin code: ')

if enter==code:
    print('Correct')
else:
    print('Incorrect..')
    enter2=input('Enter the pin code again: ')
    if enter2==code :
        print('Correct')
    else:
        print('Incorrect..')
        enter3=input('Enter the pin code again: ')
        if enter3==code :
            print('Correct')
        else:
            print('Sorry, your payment card has been blocked')
