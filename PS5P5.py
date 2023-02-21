name = str(input("What is your name? "))
salary = float(input("What is your current salary? "))
joblvl = int(input("What is your job level? "))

if joblvl >= 10:
  bonus=0.25*salary
elif joblvl>= 5:
  bonus=0.2*salary
else:
  bonus=0.1*salary

print(f"{name} it appears your bonus for the year will be ${bonus:.2f}.")