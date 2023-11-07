import mykeyboard
import mymodule

entered_number=mykeyboard.read_number()

computer_number=mymodule.generate_number()

print(f'Computer number: {computer_number}')

if entered_number==computer_number:
    print('You won the game!!')
else:
    print('You lost the game :(')