amount=float(input('Enter amount:'))
vat=amount*0.23

formatted_amount = "{:.2f}".format(amount)
formatted_vat = "{:.2f}".format(vat)

print('Amount:',formatted_amount)
print('VAT 23%:',formatted_vat)
