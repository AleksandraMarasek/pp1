a=int(input('Enter one side'))
b=int(input('Enter the other side'))

for i in range(a):
    if i==0 or i==a-1 :
        print("*"*b)
    else:
        print("*" + " " * (b - 2) + "*")