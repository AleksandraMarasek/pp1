def f(arr):
    arr.sort()
    if arr[0]<arr[1]:
        return arr[0]
    else:
        return arr[-1]
    
print(f([7,7,7,7,7,8,7,7,7]))