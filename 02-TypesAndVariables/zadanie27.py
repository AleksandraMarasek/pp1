import random

comp=random.randint(1,6)

user=int(input('Enter a random number from 1 to 6: '))

if comp==user :
    print(True)
else :
    print(False)


print('Number that the computer picked:',comp)