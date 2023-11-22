#define personal data
name="Aleksandra Marasek"
university="Krakow University of Economics"
field="Applied informatics"

file=open("student.txt","w")
file.write(name+'\n')
file.write(university+'\n')
file.write(field+'\n')

file.close()