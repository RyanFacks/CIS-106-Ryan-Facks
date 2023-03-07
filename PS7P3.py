f = open("namesal.txt","r") 
bonussum=0
lastname=str(f.readline().rstrip('\n'))

while lastname!="":
  salary=int(f.readline())
  if salary >= 100000:
    bonusrate = 0.2
  elif salary >= 50000:
    bonusrate = 0.15
  else:
    bonusrate = 0.1
  bonus = salary*bonusrate
  print(f"Name: {lastname}")
  print(f"Salary: ${salary:.2f}")
  print(f"Bonus: ${bonus:.2f}\n")
  bonussum=bonussum+bonus
  lastname=str(f.readline())
f.close()
print(f"The total amount of bonuses given out is ${bonussum:.2f}.")