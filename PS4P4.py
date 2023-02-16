appliancename = str(input("What appliance did you purchase? "))
applianceprice = float(input("What was the retail price of this appliance?"))

if applianceprice<=1000 and applianceprice > 0:
  print("This price point puts you in the 5% warranty category.")
  warranty=(0.05*applianceprice)
  appliancetotal=applianceprice+warranty
elif applianceprice>1000:
  print("This price point puts you in the 10% warranty category.")
  warranty = (0.1*applianceprice)
  appliancetotal=applianceprice+warranty
else:
  print("You can not have a negative price! Try again.")
  exit()

print(f"It appears your {appliancename} costs ${applianceprice:.2f}.")
print(f"If you purchase the warranty, the warranty will cost ${warranty:.2f}.")
print(f"Ultimately your total will be ${appliancetotal:.2f}.")