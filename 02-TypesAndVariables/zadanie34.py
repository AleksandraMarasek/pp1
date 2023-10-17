price=float(input('Enter price: '))
discount=float(input('Enter the % of the discount:'))

discount2=discount/100
discount3=1-discount2

price2=price*discount3
price3="{:.2f}".format(price2)

reduction=price-price2
reduction2="{:.2f}".format(reduction)

print('price with discounnt: ',price3)
print('reduction',reduction2)