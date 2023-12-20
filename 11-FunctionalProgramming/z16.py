'''Write a program that calculates the total value of products in stock. 
Use the map(), sum() and an anonymous function.'''


stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

total_value=float(sum(map(lambda n:n[0]*n[1],stock)))

print(total_value)