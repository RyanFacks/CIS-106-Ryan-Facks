principle = int(input("What was the initial investment? "))
rate = float(input("What was the interest rate? "))

totalint=0

for count in range(1,6,1):
  interest = principle*rate
  endbal = principle+interest
  print(f"Year: {count}   Principle: ${principle:.2f}   Ending Balance: ${endbal:.2f}")
  principle = endbal
  totalint = totalint + interest

print(f"The total interest accumulated is {totalint:.2f}.")