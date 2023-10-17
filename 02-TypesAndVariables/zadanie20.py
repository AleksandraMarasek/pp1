a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))

o=a+b+c
p=o/2
pole=(p*(p-a)*(p-b)*(p-c))**(1/2)

print('Triangle area:', pole)
print('Triangle circumference:',o)

