arr=[33,22,66,77,88]
x=arr[2] #wypisanie wartości danego elemenu z listy

arr[3]=345 #zmiana wartości danej z listy

for n in arr:
    if n%2==0:
        print(n) #elementy z listy podzielne przez 2


i=0
while i<len(arr):
    print(arr[i])
    i+=1 