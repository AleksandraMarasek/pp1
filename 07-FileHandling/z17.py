'''Find any text file on the Internet that contains at least 30 lines of text and download that file to your computer. 
Then, write a program that displays the first five lines from the file and then waits for the Enter key to be pressed. 
The program repeats displaying the next five lines from the file, waiting for the Enter key to be pressed each time.'''

filename = "inwokacja.txt"

with open(filename, 'r', encoding='UTF-8') as file:
    lines = file.readlines()

line_count = len(lines)
lines_per_iteration = 5
current_line = 0

while current_line < line_count:
    for i in range(lines_per_iteration):
        if current_line + i < line_count:
            print(lines[current_line + i], end="")
    
    input("Press Enter to continue...")
    current_line += lines_per_iteration