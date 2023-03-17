def compmpg(gallons,miles):
  mpg = miles/gallons
  return float(mpg)
def gascost(gallons):
  gascost = gallons*2.5
  return gascost

city = str(input("What city are you traveling to? "))
miles = int(input(f"How many miles will you approximately travel to {city}? "))
gallons = int(input("How many gallons of fuel approximately will your car use? "))

mpg=compmpg(gallons,miles)
gascost=gascost(gallons)

print(f"When traveling to {city} you will travel {miles} miles and the gas will cost ${gascost:.2f}.  Your miles per gallon will be {mpg:.2f}.")