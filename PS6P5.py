discountsum = 0

response = str(input("Do you want to run this program? ('yes' or 'no') "))
while response == 'yes':
  qty = int(input("How many units did you buy? "))
  ppu = float(input("How much did each unit cost? "))
  extendedprice = ppu*qty
  if extendedprice>10000:
    discount = extendedprice*0.25
  else:
    discount = extendedprice*0.1
  total = extendedprice-discount
  print(f"Your extended price is ${extendedprice:.2f} and your discount is ${discount:.2f}.  This means your total is ${total:.2f}.")
  discountsum = discountsum+discount
  response = str(input("Do you want to run this program again? ('yes' or 'no') ")) 


print(f"The sum of all the discounts is ${discountsum:.2f}.")