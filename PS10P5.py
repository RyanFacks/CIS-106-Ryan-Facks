qty = int(input("How many items were purchased?" ))
price = float(input("What was the price of the items? "))

total=0.0
tax=0.0

def compute(qty,price):
  global total
  total=qty*price
  global tax
  tax=total*0.07
  return
compute(qty,price)
print(f"The extended price is ${total:.2f} and the tax will be ${tax:.2f}.")