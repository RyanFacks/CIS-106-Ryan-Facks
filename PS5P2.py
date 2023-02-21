#I chose to make the Part# an integer rather than a string for simplicity.

partid = int(input("What is the ID# of the part you purchased? "))
qty = int(input("How many did you purchase? "))

if partid == 10 or partid == 55:
  unitcost = 1
elif partid == 99:
  unitcost = 2
elif partid == 80 or partid ==70:
  unitcost = 3
else:
  unitcost = 5

total=qty*unitcost

print(f"You purchased part #{partid} which has a value of ${unitcost:.2f} per unit.\nBecause you purchased {qty} parts, your total is ${total:.2f}.")