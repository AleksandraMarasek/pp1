def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

def find_primes(N):
    prime_numbers = []
    number = 2

    while len(prime_numbers) < N:
        if is_prime(number):
            prime_numbers.append(number)
        number += 1

    return prime_numbers

try:
    N = int(input("Enter the number of prime numbers you want to find: "))
    if N < 1:
        print("Please enter a positive integer greater than or equal to 1.")
    else:
        prime_numbers = find_primes(N)
        print(f"The first {N} prime numbers are: {prime_numbers}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")