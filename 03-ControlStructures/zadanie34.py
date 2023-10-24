decimal = int(input("Enter a decimal number: "))

def decimal_to_binary(decimal):
    binary = " "

while decimal>0:
    remainder=decimal/2
    binary = str(remainder) + binary
    decimal = decimal // 2


if decimal < 0:
    print("Please enter a non-negative decimal number.")
else:
    binary = decimal_to_binary(decimal)
    print(f"The binary representation of {decimal} is: {binary}")



