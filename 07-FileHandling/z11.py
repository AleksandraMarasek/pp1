numbers=open('numbers.txt','r')

sum=0

for i in numbers:
    sum += int(i)
    print(i, end="")
print()    
print(f'Sum: {sum}')

numbers.close()
