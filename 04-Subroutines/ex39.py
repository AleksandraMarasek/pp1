def f(number):
    number_str = str(number)
    digit_counts = {}

    for digit in number_str:
        if digit.isdigit():
            digit_counts[digit] = digit_counts.get(digit, 0) + 1

    repeated_digit_sum = 0
    for count in digit_counts.values():
        if count > 1:
            repeated_digit_sum += int(count)

    return repeated_digit_sum

print(f(230335))