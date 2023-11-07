def f(password):
    if len(password)<6:
        return False
    
    return len(set(password)) >=6


print(f("asf1234"))