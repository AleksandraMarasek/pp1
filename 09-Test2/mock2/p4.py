def f(subjects):
    max_subject=0
    result=0

    for subject,grades in subjects.items(): #otwieranie słownika
        average=sum(grades)/len(grades) #średnia ocen

        if average>max_subject:
            max_subject=average #zapisywanie każdej najwyższej wartości w 'max subject' jeśli jest wyższa niz poprzednia average
            result=subject #key(subject) do value(grades)
    
    return result
        

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})  )
