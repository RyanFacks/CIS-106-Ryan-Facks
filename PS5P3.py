principle = int(input("What was the principle amount invested? "))
maturity = int(input("How many years will it take to mature? "))

if principle == 100000 and maturity == 5:
  interest = 0.06
elif principle == 50000 and maturity == 10:
  interest = 0.05
elif principle == 50000 and maturity == 5:
  interest = 0.04
else:
  interest = 0.02

firstyear = principle*interest

print(f"You invested a principle amount of ${principle:.2f} and it will take {maturity} years to mature.\nThis puts you at an interest rate of {interest:.1%}. After one year you will have gained ${firstyear:.2f} in interest.")