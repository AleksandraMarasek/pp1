array = [2,3,7,5,4]
print(f'The array: {array}')

b=len(array)
print(f'Number of elements: {b}')

c=array[0]
print(f'First element: {c}')

d=array[1]
print(f'Second element: {d}')

e=array[(len(array)-1)]
print(f'Last value: {e}')

f=array[(len(array))-2]
print(f'Last but one value: {f}')

g=array[0]+array[-1]
print(f'Sum of the first and last value: {g}')

h='2'
print(f'Middle value: {h}')

print('All array values separated by a single space: ')
for i in array:
    
    print(i,end=" ")

