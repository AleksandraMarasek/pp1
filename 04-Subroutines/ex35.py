def f(detector):
    
    current_people=0
    max_people=0
    
    for person in detector:
        if person=="+":
            current_people+=1
            max_people=max(max_people,current_people)
        elif person=='-':
            if current_people<0:
                current_people-=1
    return max_people >=3


print(f("+-+++-+---"))
