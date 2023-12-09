'''Write a program that calculates the number of vowels in the text:
To be, or not to be, that is the question
Use regular expressions and the findall() method.
'''
import re

def vowels(text):
    vowel_pattern = re.compile(r'[aeiou]', re.IGNORECASE)
    vowels = vowel_pattern.findall(text)

    num_vowels = len(vowels)

    return num_vowels

file=input('enter file name: ')

result=(vowels(file))

print(f'number of vowels: {result}')