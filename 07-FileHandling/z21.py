'''⦁	Create a program that writes 50 random integers between 100 and 999 to a text file, 
each number on a separate line.
'''
import random

file='random_numbers.txt'
randomsy=[random.randint(100,999) for x in range(50)]

with open(file,'w') as file1:
    for n in randomsy:
        file1.write(f'{n}\n')
    
    

file1.close()