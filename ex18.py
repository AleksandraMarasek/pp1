n=int(input('Enter number: '))

def numbers(x):
    for i in range(1,(x+1)):
        print(i, end=' ')    
    
print(f'Numbers <1,{n}>: {numbers(n)}')