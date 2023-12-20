'''19.	The final grades obtained by students in the "Economic Geography" course are included in the array:
Write a program that calculates the arithmetic mean of the grades, excluding negative grades (2.0). 
Use the filter() along with an anonymous function.
'''

grades=[3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

a_mean=round(sum(list(filter(lambda grade:grade>2.0,grades)))/len(list(filter(lambda grade:grade>2.0,grades))),2)

print(a_mean)