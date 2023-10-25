n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
n3=int(input('Enter third number: '))


def different(x,y,z):
    if x!=y and x!=z and y!=z :
        return True
    else:
        return False

print(different(n1,n2,n3))


