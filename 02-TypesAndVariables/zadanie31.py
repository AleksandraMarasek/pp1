buy=float(input('Bank buys EUR: '))
sell=float(input('Bank sells EUR: '))

spread=buy-sell

spread2="{:.4f}".format(spread)

print('Bank buys EUR: ',buy)
print('Bank sells EUR: ',sell)
print('Spread: ',spread2)