def f(name):
    words=name.split()
    result=''.join(word[0] for word in words)
    return result

print(f('Internet of Things'))