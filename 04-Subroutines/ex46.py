def f(product_code):
    if len(product_code)!=4 :
        return False
    if not product_code.isdigit():
        return False
    
    if len(product_code)==4:
        first3=product_code[:3]
        last1=product_code[3]

        first3sum=sum(int(digit) for digit in first3)
        computed_control_digit = str(first3sum % 7)

    return last1==computed_control_digit   

print(f("1082"))
    

