# Initialize the first two terms of the sequence
a, b = 0, 1

# Initialize a list to store the Fibonacci sequence
fibonacci_sequence = [a, b]

# Generate the next 18 terms of the sequence
for i in range(18):
    # Calculate the next term by adding the previous two
    a, b = b, a + b
    fibonacci_sequence.append(b)

# Display the first twenty terms of the Fibonacci sequence
for i, term in enumerate(fibonacci_sequence):
    print('{term}')
