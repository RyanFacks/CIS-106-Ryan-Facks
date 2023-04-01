summsrp = 0
sumtotal=0
response = str(input("Do you want to run this program? ('Yes' or 'No')"))

def odprice(msrp,make,model,evcode):
  if make.lower() in "honda" and model.lower() in "accord":
    percentoff = 0.1
  elif make.lower() in "toyota" and model.lower() in "rav4":
    percentoff = 0.15
  elif evcode.lower() in "yes":
    percentoff = 0.3
  else:
    percentoff=0.05
  discount=percentoff*msrp
  newmsrp = msrp - discount
  msrpwtax = newmsrp*1.07
  return float(msrpwtax)

while response.lower() in "yes":
  make = str(input("What is the make of the car? "))
  model = str(input("What is the model of the car? "))
  evcode = str(input("Is the car electric? ('Yes' or 'No')"))
  msrp = float(input("What is the MSRP of the vehicle? "))
  summsrp = summsrp + msrp
  float(summsrp)
  msrpwtax=odprice(msrp,make,model,evcode)
  float(msrpwtax)
  sumtotal = sumtotal+msrpwtax
  print(f"The MSRP after discount and tax is ${msrpwtax:.2f}.")
  response = str(input("Do you want to run this program again? ('Yes' or 'No')"))
print(f"The total of MSRPs before discount and tax is ${summsrp:.2f} and the total of MSRPs after discount and tax is ${sumtotal:.2f}.")