'''10.	Write a program that calculates the average speed of a vehicle. 
Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. Define a function avg_speed(distance,hours,minutes) that returns the calculated average speed. '''


def avg_speed(distance,hours,minutes):
    h=hours+(minutes/60)
    result=distance/h
    
    return round(result,1)

if __name__=="__main__":
    print(f"Average speed: {avg_speed(70,1,23)} km/h")
