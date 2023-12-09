'''Write a program that calculates the number of lines for any text file. 
The user enters the name of the file from the keyboard. 
Display the result of the calculation 
(the file name and the number of lines). 
Do not display the contents of the file.
'''

file=input('Enter file name: ')
file1=open(file)

counter=0

for line in file1:
    if line!="":
        counter+=1
    else:
        counter+=0

print(f'File name: {file}')
print(f'Number of lines: {counter}')

file1.close()