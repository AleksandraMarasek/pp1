wzrost=int(input('Enter your height in cm'))
waga=int(input('Enter your weight in kg'))

wzrost2=wzrost/100

bmi=waga/wzrost

print('Your BMI Index:', bmi)
if bmi>18.5 and bmi<24.9 :
    print('Correct weight: True')
else:
    print('Correct weight: False')