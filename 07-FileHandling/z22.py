'''Create a program that saves to a text file integer numbers 
in the range <1,10> with their second and third power. '''


file=('numbers_power.txt')

with open(file, 'w') as file1:
    for i in range(1,11):
        file1.write(f'{i}, {i**2}, {i**3},\n')

file1.close()
