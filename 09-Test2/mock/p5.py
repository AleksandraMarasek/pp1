import re

def f(first_letter,last_letter):
    with open('data.txt','r') as file:
        content=file.read()

        pattern=r'\b{}\w*{}\b'.format(first_letter, last_letter)
        result=re.findall(pattern,content)
        return len(result)

print(f('w','d'))