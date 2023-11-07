def f(x,y,z):
    x= True if x or y or z < 0 else False
    return x

a=input('enter number: ')
b=input('enter number: ')
c=input('enter number: ')

print(f(a,b,c))