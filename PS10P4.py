def gamescore(s1,s2,s3,handicap):
  avgscore=(s1+s2+s3)/3
  hcscore=(s1+s2+s3+handicap)/3
  return avgscore,hcscore

lname=str(input("What is the bowler's last name? "))
s1 = float(input("What is the first game's score? "))
s2=float(input("What is the second game's score? "))
s3=float(input("What is the third game's score? "))
handicap=float(input("If there is a handicap, what is it?"))
avgscore,hcscore=gamescore(s1,s2,s3,handicap)
print(f"The bowler {lname} has an average score of {avgscore} and the handicap score is {hcscore}.")