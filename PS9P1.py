response = str(input("Do you want to run this program ('Yes' or 'No')?" ))

def comppercent(month,sales):
  if month.lower() in ["jan","feb","mar"]:
    percent = 0.1
  elif month.lower() in ["apr","may","june"]:
    percent = 0.15
  elif month.lower() in ["jul","aug","sept"]:
    percent = 0.2
  elif month.lower() in ["oct","nov","dec"]:
    percent = 0.25
  else:
    print("Please enter a valid month abreviation" )
    exit()
  
  nextmonthsales=(percent+1)*sales
  return nextmonthsales

while response.lower() == "yes":
  lname = str(input("What is your last name? "))
  month = str(input("What month is it? "))
  sales = float(input("What are the current sales? "))
  nextmonthsales = comppercent(month,sales)
  
  print(f"Your name is {lname} and for the month of {month} the forecasted sales are ${nextmonthsales:.2f}.")
  response = str(input("Do you want to run the program again? ('Yes' or 'No')" ))

print("Now exiting program.")
exit()
  