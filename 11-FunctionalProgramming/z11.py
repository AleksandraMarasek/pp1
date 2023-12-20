'''11.	Write a program that calculates the average speed of a vehicle. 
Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. 
Use an anonymous function. 
'''

x= lambda distance,hours,minutes: round(distance/(hours+(minutes/60)),1)

print(f"Average speed: {x(70,1,23)} km/h")