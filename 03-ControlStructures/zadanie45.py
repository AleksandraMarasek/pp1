total = 0
count = 0

# Continuously prompt the user for input and calculate the sum
while True:
    try:
        num = float(input("Enter number: "))
        if num == 0:
            break  # Exit the loop when 0 is entered
        total += num
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate the arithmetic mean (average)
if count > 0:
    mean = total / count
else:
    mean = 0

# Display the result
print(f"RESULT: Quantity={count}, Sum={total}, Mean={mean}")