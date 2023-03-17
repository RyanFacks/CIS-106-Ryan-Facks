def computetotal(qty,price):
  total=float(qty)*float(price)
  if total>10000:
    total=total*0.9
  else:
    total=total
  return total

qty = float(input("Please enter the number of items purchased: "))
price = float(input("What was the price per unit? "))

total=computetotal(qty,price)

print(f"You ordered {qty} number of items. Each item cost ${price:.2f} This results in a total of ${total:.2f}.")