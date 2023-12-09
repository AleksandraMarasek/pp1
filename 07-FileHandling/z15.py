filename="inwokacja.txt"

with open(filename, 'r', encoding='UTF-8') as f:
    for line in f:
        print(line, end="")