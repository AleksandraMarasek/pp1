washing_product=str(input('Enter product that you want to wash, form the lost provided (jacket/underwear/shoes): '))
rinse=str(input('Do you want to have an additional rinse? (yes or no): '))
spin=str(input('Do you want to add an additional spin? (yes or no): '))

if rinse=='yes' :
    rinse=True
    rinse_time=15
else:
    rinse=False
    rinse_time=0

if spin=='yes' :
    spin=True
    spin_time=9
else:
    spin=False
    spin_time=0

if washing_product=='shoes':
    washing_time=20

if washing_product=='jacket':
    washing_time=40

if washing_product=='underwear':
    washing_time=70

total=rinse_time+spin_time+washing_time

print(f'Total washing time: {total} minutes')