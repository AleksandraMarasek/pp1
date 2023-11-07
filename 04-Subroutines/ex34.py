def f(n1,n2,op):
    if op=='+':
        result=n1+n2
    elif op=='-':
        result=n1-n2
    elif op=='*':
        result==n1*n2
    elif op=='//':
        result=n1//n2
    return result

x=int(input('Enter number: '))
y=int(input('Enter number: '))
z=input('Enter operator(+,-,*,/): ')

print(f(x,y,z))

