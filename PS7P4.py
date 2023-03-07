c = open("widget.txt","r")
count = 0
extpricesum = 0
itemid=str(c.readline().rstrip('\n'))
print("Order Summary: \n")

while itemid !="":
  qty=int(c.readline())
  price=int(c.readline())
  extprice=qty*price
  extpricesum=extpricesum+extprice
  count=count+1
  print(f"Item: {itemid}")
  print(f"Quantity: {qty}")
  print(f"Price: ${price:.2f}")
  print(f"Total Price: ${extprice:.2f}\n")
  itemid=str(c.readline())
c.close()
avg = extpricesum/count

print(f"The sum of all orders is ${extpricesum:.2f}")
print(f"There were {count} number of orders")
print(f"The average order is ${avg:.2f}")