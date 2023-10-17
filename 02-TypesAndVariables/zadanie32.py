gender=input('Pick Mr or Mrs:')

name=input('Enter your name: ')
surname=input('Enter your last name: ')
date=input('Enter your date of birth: ')

print(f'Description: {gender} {name} {surname}, born on {date}')
print('Name:',name)
print('Surname',surname)
print('Initials:',name[:1],surname[:1])
print('Date of birth:',date)