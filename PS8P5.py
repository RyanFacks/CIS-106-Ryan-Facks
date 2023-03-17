def comptuition(dcode,credits):
  if "I" in dcode:
    tuition = credits*250
  elif "O" in dcode:
    tuition=credits*550
  else:
    print("Please enter either 'I' or 'O'")
    exit()
  return tuition

lname=str(input("What is the students last name? "))
credits=int(input(f"How many credits is {lname} taking? "))
dcode=str(input("Is the student in district or out of district? ('I' or 'O') "))

tuition=comptuition(dcode,credits)

print(f"The student {lname} owes ${tuition:.2f} in tuition")