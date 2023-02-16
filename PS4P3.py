books = int(input("We are having a free shipping deal if your order is over $50! How many books did you purchase? "))
bookscost = float(input("How much did each book cost? "))

ordertotal = books*bookscost

if ordertotal <= 50.00:
  shipping=25
  totalwshipping=ordertotal+shipping
else:
  totalwshipping=ordertotal
  shipping=0
  
print(f"Your total is ${ordertotal:.2f} and shipping is ${shipping:.2f}.")
print(f"Your total with shipping is ${totalwshipping:.2f}.")