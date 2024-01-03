'''def f(years,course):
    import json
    with open(course,'r') as file:
        addf=file.read()
        sum=0
        x=json.loads(addf)
        for i in x:
            for key,value in i.items():
                if key=="age" and value>years:
                    for key1,value1 in i.items():
                        if key1=="studies":
                            for key2,value2 in value1.items():
                                if key2=="courses":
                                    for y in value2:
                                        for key3,value3 in y.items():
                                            return 2
                                        '''
                                                   
                                               
def f(years,course):
    import json
    with open('data.json')as jsf:
        file=json.load(jsf)

    filtered=[student for student in file if student>=['age']]     
    counter=0

    for student in filtered:
        for info in student['studies']['courses']:
            if info['name']==course and all(grade >= 4 for grade in info['grades']):
                counter+=1
    return counter                    
                
print(f(21,"statistics")) #nie działa
    
    
#print(f(10,'data.json'))