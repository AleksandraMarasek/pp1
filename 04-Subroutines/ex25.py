compare_numbers= lambda n1,n2 : True if n1>n2 else False

p1=(34,25)
p2=(19,23)

r1=compare_numbers(p1[0],p1[1])
r2=compare_numbers(p2[0],p2[1])

print(f'Is {p1[0]} greater than {p1[1]}? : {r1}')
print(f'Is {p2[0]} greater than {p2[1]}? : {r2}')