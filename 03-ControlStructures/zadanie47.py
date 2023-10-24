min_number = 1
max_number = 49
num_rows = 7
num_columns = 7

# Calculate the width needed for formatting (based on the maximum number)
column_width = len(str(max_number))

# Initialize the current number
current_number = min_number

# Loop to generate and display the lottery coupon
for row in range(num_rows):
    for column in range(num_columns):
        # Print the current number, right-aligned within the column width
        print(f"{current_number:>{column_width}}", end=" ")
        
        # Calculate the next number
        current_number += 1
        
        # Stop when we reach the maximum number
        if current_number > max_number:
            break
    print()  # Move to the next line after each row