name = str(input("What is your last name? "))
numdependents = int(input("How many dependnets do you have? "))
grossincome = float(input("What is your anual gross income? "))

adjustedincome=grossincome-(numdependents*12000)

if adjustedincome > 0 and adjustedincome <=50000:
  tax=0.1
  incometax=tax*adjustedincome
elif adjustedincome > 50000:
  tax =0.2
  incometax=tax*adjustedincome
else:
  incometax=100

print(f"Mr/Mrs. {name}, your gross income is ${grossincome:.2f} and you have {numdependents} dependents.")
print(f"Your adjusted gross income is ${adjustedincome:.2f} and your income tax is ${incometax:.2f}.")