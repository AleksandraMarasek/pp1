import module24

number1=int(input('Range number: '))
number2=int(input('Range number: '))
number3=int(input('Number to be checked: '))

result=module24.number(number1,number2,number3)

print(f'Number {number3} in the range <{number1},{number2}>: {result}')