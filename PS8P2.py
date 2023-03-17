def compbatavg(atbats,numhit):
  batavg = float(numhit)/float(atbats)
  return batavg

lname = str(input("What is the player's last name? "))
atbats = float(input("How many times was the player at bat? "))
numhit = float(input("How many hits did the player have? " ))

batavg = compbatavg(atbats,numhit)
print(f"The player {lname} has a batting average of {batavg:.3f}.")