def f(x,y):
    list=0
    for i in range(x,y):
        if i < 0 and i%2==0:
            list+=1
    return list        

a=input('x = ')
b=input('y = ')

result= f(a,b)

print(result)