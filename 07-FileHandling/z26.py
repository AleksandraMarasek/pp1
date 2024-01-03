def f(text):
    import re
    counter=0
    pattern=rf"^[a-zA-Z]$"
    for words in text:
        if re.match(pattern, text):
            counter+=1
    return counter

print(f("To be, or not to be, that is the question"))