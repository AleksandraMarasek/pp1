n=int(input("Enter month number: "))

def month(x):
    months=['january','February','March','April','May','June','July','August','September','October','November','December']
    return months[n-1]  
    
result=month(n)

print(f'Month name: {result}')

