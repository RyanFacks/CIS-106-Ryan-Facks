widgetqty = int(input("How many widgets did you purchase?"))

if widgetqty > 10000:
  extendedprice = widgetqty*10
elif widgetqty >= 5000:
  extendedprice = widgetqty*20
elif widgetqty >= 0:
  extendedprice = widgetqty*30
else:
  print("You cannot have a negative widget value. Try again.")
  exit()

taxamount = extendedprice*0.07
totalprice = extendedprice+taxamount

print(f"Since you have purchased {widgetqty} widgets, your extended price is ${extendedprice:.2f}")
print(f"With tax at 7%, you will pay ${taxamount:.2f} and your total price will be ${totalprice:.2f}.")