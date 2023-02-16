numpurchased = int(input("How many items did you purchase? "))
aorb = str(input("Did you purchase item A or item B? "))

if ('a' or 'A') in aorb:
  extprice=numpurchased*10.00
  unitprice = 10.00
elif ('b' or 'B') in aorb:
  extprice = numpurchased*20.00
  unitprice = 20.00
else:
  print("You must state item 'a' or 'b'. Try again.")

print(f"You purchased {numpurchased} items at ${unitprice:.2f} a unit.  This results in your extended price being ${extprice:.2f}.")