def report(sales):
  if sales>100000:
    commissionrate=0.1
  elif sales <=100000:
    commissionrate=0.05
  commission=sales*commissionrate
  target=sales*1.05
  return target,commission

lname = str(input("What is the salesperson's name? "))
sales = float(input("What is the salesperson's name? "))
target,commission = report(sales)
print(f"{lname} had ${sales:.2f} in sales.  This results in a commission of ${commission:.2f} and next year's target is ${target:.2f}.")