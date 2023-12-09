'''Create a program that writes to a text file 
integer numbers in the range <1,50>, every number in a separate line.
'''

file=open('integer_numbers.txt','w')

for i in range(1,51):
    file.write(f'{i}\n')

file.close()

print('DONE')