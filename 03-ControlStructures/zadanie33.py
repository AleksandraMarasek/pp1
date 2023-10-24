science=str(input('Are you interested in computer science? (Y/N): '))
games=str(input('Do you like playing video games? (Y/N):'))
insta=str(input('Do you have an instagram account? (Y/N): '))

if science=='Y':
    print('Interested in computer science: Yes')
elif science=='N':
    print('Interested in computer science: No')
else:
    print('Interested in computer science: Invalid answer')

if games=='Y':
    print('Playing computer games: Yes')
elif games=='N':
    print('Playing computer games: No')
else:
    print('Playing computer games: Invalid answer')

if insta=='Y':
    print('Has an instagram account: Yes')
elif insta=='N':
     print('Has an instagram account: No')
else:
     print('Has an instagram account: Invalid answer')