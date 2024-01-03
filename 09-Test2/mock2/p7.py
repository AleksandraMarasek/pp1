def f(arr):
    import re
    counter=0
    for username in arr:
        pattern=r'^[a-z0-9_]{4,12}$' #początek wyrażenia-'dozwolone znaki'-ilość znaków-koniec
        if re.match(pattern,username):#elementy spełniające dany warunek
            counter+=1
    return counter          
                    
            

print(f((["uek","water_7_x","anna.may","a_b_c_d_e_f"])  ))