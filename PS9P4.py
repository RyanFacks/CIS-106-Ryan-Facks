tsum=0
response=str(input("Do you want to run this program? ('Yes' or 'No')"))

def ticket(miles):
  if miles >=30:
    tprice=12
  elif miles>=20:
    tprice=10
  elif miles>=10:
    tprice=8
  else:
    tprice=5
  return tprice

while response.lower() in "yes":
  lname = str(input("What is your last name? "))
  miles = int(input("How many miles are you from downtown Chicago? "))
  tprice=ticket(miles)
  tsum=tsum+tprice
  print(f"{lname}'s' train ticket will cost ${tprice:.2f} to get to Chicago.")
  response= str(input("Do you want to run this program again? ('Yes' or 'No')"))

print(f"The sum of all the train tickets is ${tsum:.2f}.")