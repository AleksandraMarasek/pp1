'''An array contains at least 3 integers. 
All numbers in the array are equal except one. 
Create a function f(arr) that returns a number in the arr array 
that is different from the other numbers. '''

def f(arr):
    arr.sort()
    
    if arr[0]<arr[1]:
        return arr[0]
    else:
        return arr[-1]
    

print(f([7,7,7,7,7,8,7,7]) )

print(f([3,3,3,3,3,7,3,3]))