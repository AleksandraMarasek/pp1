'''The announcement regarding the temperature forecast in degrees Celsius
for the next three days was published on the Internet:

"Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

Create a program that calculates the average temperature. 
Use regular expressions to extract the values of temperatures from the message.
'''
import re

announcments="Tuesday: 22C, Wednesday: 21C, Thursday: 26C"

temperature_pattern = re.compile(r'\b\d{1,2}C\b')
matches = temperature_pattern.findall(announcments)

temperatures = [int(match[:-1]) for match in matches]
average_temperature = sum(temperatures) / len(temperatures)

print("Temperatures:", temperatures)
print("Average Temperature:", average_temperature, "C")

