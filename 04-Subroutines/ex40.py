def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

def f(n):
    if n <= 0:
        return None

    prime_count = 0
    num = 2  # Start with the first prime number
    while prime_count < n:
        if is_prime(num):
            prime_count += 1
        if prime_count < n:
            num += 1

    return num