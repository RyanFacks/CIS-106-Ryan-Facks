numticket = int(input("How many tickets did we sell? "))

if numticket >= 25:
  ppt=50
elif numticket >=10:
  ppt=60
elif numticket>=5:
  ppt=70
elif numticket>=0:
  ppt=75
else:
  print("You can not have a negative value of tickets!")
  exit()

total = ppt*numticket

print(f"The number of tickets sold is {numticket} and each ticket is ${ppt:.2f} per ticket.\nThe total cost is ${total:.2f}")