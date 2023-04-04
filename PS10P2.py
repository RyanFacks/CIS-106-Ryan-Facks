def examscore(s1,s2,s3):
  avgscore=(s1+s2+s3)/3
  totalscore = s1+s2+s3
  return avgscore,totalscore

lname = str(input("What is the student's last name? "))
s1 = float(input("What is the student's first score? "))
s2=float(input("What is the student's second score? "))
s3=float(input("What is the student's third score? "))
avgscore,totalscore=examscore(s1,s2,s3)
print(f"{lname}'s scores total to {totalscore} and average at {avgscore}.")