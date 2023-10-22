price=float(input('Enter priducts price: '))
discount=float(input('Enter the % the price is discounted by: '))
discount2=discount/100

discount3=1-discount2

price2=price*discount3
price3="{:.2f}".format(price2)

if price2<=(price*0.9) :
    print('Buy the product!!')
else:
    print('We do not reccomend buying the product')

print(f'Current product price: {price3}')
print(f'previous product price: {price}')
print(f'Product price reduced by {discount}%')