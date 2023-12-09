'''Find any text file on the Internet and download it to your computer. 
Then write a program that copies the contents of this file to the copy.txt file. 
Copy the contents of the file as a whole. 
Finally, open both files in any text editor and check that their contents are the same.
'''



file1=open('inwokacja.txt', 'r', encoding='UTF-8')
file11=str(file1.read())

file2=open('copy.txt','w',encoding='UTF-8')

file2.write(file11)

file1.close()
file2.close()