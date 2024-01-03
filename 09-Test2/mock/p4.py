def f(subjects):
    max_subject= None
    max_average=0
    for subject,grades in subjects.items():
        average=sum(grades)/len(grades)
        if average > max_average:
            max_average = average
            max_subject = subject

    return max_subject


result = f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})
print(result)