def f():
    import re
    suma=0
    with open('grades.txt','r') as file:
        pattern=r"\d\.\d"
        grades=re.findall(pattern, file.read())
        sum=0
        for i in grades:
            sum+=float(i)

        return(round(sum/len(grades), 2))


print(f())