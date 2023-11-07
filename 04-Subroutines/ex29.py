def f(number, even):
    total = 0
    zero = 0
    while number > zero:
        digit = number % 10
        number //= 10
        if (even and digit % 2 == 0) or (not even and digit % 2 != 0):
            total += digit
    return total

n = int(input('Enter number:'))
x = input('Do you want to count even or uneven digits? (y/n) ')

y = True if x == 'y' else False

print(f(n, y))