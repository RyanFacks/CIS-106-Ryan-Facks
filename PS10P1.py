def discounts(qty,price,discrate):
  extprice = qty*price
  discamt=extprice*discrate
  discprice=extprice-discamt
  return discamt,discprice

qty = int(input("How many items were sold? "))
price = float(input("What is the price of the items? "))
discrate = float(input("What is the discountrate? "))
discamt,discprice=discounts(qty,price,discrate)
print(f"{qty} items were purchased at a price of ${price:.2f}.  The discounted amount is ${discamt:.2f} and the discounted price is ${discprice:.2f}.")