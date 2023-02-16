#This is a program that will take items purchased as an input
#Based on this input, a conditional statement will determine whether price is $3 or #5
#Calculations will result in displaying quantity purchased, price per unit, extended price, total tax, and final value owed (extendedprice + tax)

itemspurchased = int(input("How many items did you purchase?\n"))

if itemspurchased >= 1000:
  itemprice = 3.00
  extendedprice = itemspurchased*itemprice
  tax = extendedprice*0.07
  total = extendedprice + tax
else:
  itemprice = 5.00
  extendedprice = itemspurchased*itemprice
  tax = extendedprice*0.07
  total=extendedprice+tax

print(f"You purchased {itemspurchased} items at ${itemprice:.2f} a unit.\n")
print(f"Your extended price is ${extendedprice:.2f}.\n")
print(f"You will have to pay ${tax:.2f} in taxes.\n")
print(f"At 7% tax you will ultimately pay ${total:.2f}")