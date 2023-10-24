import random

# Set the range and the number of random numbers
lower_limit = 5
upper_limit = 10
num_numbers = 20

# Generate and display 20 random numbers in the specified range
random_numbers = [random.randint(lower_limit, upper_limit) for _ in range(num_numbers)]

print("Random Numbers:")
for number in random_numbers:
    print(number, end=" ")