ean=str(input('Enter EAN-13 article number: '))

if len(ean)==13 :
    print('Article number is correct')
else:
    print('Article number is incorrect')


if ean.startswith('590') :
    print('Article manufactured in Poland')
else:
    print('The product was not manufactured in Poland')