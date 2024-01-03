from collections import Counter

def f(arr):
    count_dict=Counter(arr)
    for num,count in count_dict.items():
        if count==1:
            return num
        
array=[7,7,7,7,7,5,7,7]

print(f(array))