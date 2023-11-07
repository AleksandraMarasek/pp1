import letter_counting

text_input=input('Enter chosen text: ')
letter_input=input('Pick which letter you want to be counted: ')

result=letter_counting.letter_counting(text_input,letter_input)

print(f'The number of letter {letter_input}: {result}')