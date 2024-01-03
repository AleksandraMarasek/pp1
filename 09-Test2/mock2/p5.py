def f(first_letter,last_letter):
    import re

    with open('data.txt','r',encoding='UTF=8') as file:
        content=file.read()

        pattern=rf'\b{first_letter}[\w-]*{last_letter}\b' #pattern=r'\b{}\w*{}\b'.format(first_letter, last_letter)
        #\b-wyszukiwanie pojedynczego słowa-{}miejsce gdzie(.format) wstawi daną wartość-\w dowolny znak 

        result=re.findall(pattern,content ,re.IGNORECASE) #znajduje wszystkie słowa które pasuja do wzoru i dodaje je do listy
        
        return len(result) #długość listy
    
print(f('w','d'))