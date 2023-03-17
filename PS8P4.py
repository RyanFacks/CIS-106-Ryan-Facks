def determinegross(hours,payrate):
  if hours > 40:
    overtimehours=hours-40
    grosspay=(40*hours)+(overtimehours*1.5)
    return grosspay
  else:
    grosspay=hours*payrate
    return grosspay

def determinepay(jcode):
  if "L" in jcode:
    payrate=25
  elif "A" in jcode:
    payrate=30
  elif "J" in jcode:
    payrate=50
  else:
    print("You must enter 'L' 'A' or 'J'.")
    exit()
  return payrate

lname = str(input("What is your last name? ")) 
jcode = str(input("What is your job code? ('L' 'A' or 'J') "))
hours = int(input("How many hours did you work? "))

payrate = determinepay(jcode)
grosspay= determinegross(hours,payrate)

print(f"Your name is {lname} and your gross pay is ${grosspay:.2f}.")
