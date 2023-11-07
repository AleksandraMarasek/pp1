def f(number,even):
    number_str=str(number)
    evens=0
    unevens=0
    for i in number_str:
        digit=int(digit)
        if even and digit % 2 == 0 :
            evens += digit
        elif not even and digit % 2 == 1 :
            unevens+= digit
    return evens if even else unevens