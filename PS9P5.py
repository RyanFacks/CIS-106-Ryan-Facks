summv=0
sumav=0

def assessvalue(mvh,county):
  if county.lower() in "cook":
    avpercent = 0.9
  elif county.lower() in "dupage":
    avpercent = 0.8
  elif county.lower() in "mchenry":
    avpercent = 0.75
  elif county.lower() in "kane":
    avpercent = 0.6
  else:
    avpercent = 0.7
  assessedvalue = avpercent*mvh
  return assessedvalue

response = str(input("Do you want to run this program? ('Yes' or 'No')"))
while response.lower() in "yes":
  county = str(input("What county is the home in? "))
  mvh = float(input("What is the market value of the home? "))
  assessedvalue = assessvalue(mvh,county)
  summv = summv + mvh
  sumav = sumav + assessedvalue
  print(f"\nThe assessed value of the home is ${assessedvalue:.2f}.")
  response = str(input("\nDo you want to run this program again? ('Yes' or 'No')"))
print(f"\nThe sum of all the home's market values is ${summv:.2f} and the sum of all the assessed values is ${sumav:.2f}.")