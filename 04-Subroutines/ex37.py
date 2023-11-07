def f(palindrome):
    result = True if palindrome==reversed(palindrome) else False
    return result

print(f("book"))