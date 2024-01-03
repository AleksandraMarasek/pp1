def f(subjects):
    max_average=0
    result=0
    for subject,grade in subjects.items():
        average=sum(grade)/len(grade)
        if average>max_average:
            max_average=average
            result=subject

    return result

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})  )

