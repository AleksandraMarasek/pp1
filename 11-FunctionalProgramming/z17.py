'''Save the list of employees in a string array. 
Then, write a program that displays people whose surnames start with the letter 'J'. 
Use anonymous and filter() functions.'''


employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
             "JACKSON Peter","JOHNSON Rick",
             "LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e:e[0]=="J", employees)) 
#podczas filtrowania 'wynik' lambdy musi zwrócić True albo False
