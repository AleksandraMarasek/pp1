def acronym(name):
    words = name.split()  # Split the input text into words
    result = ''.join(word[0] for word in words if word.isalpha()).upper()
    return result

print(acronym("Attack on Titan"))