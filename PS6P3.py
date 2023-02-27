response = str(input("Do you want to run this program? ('yes' or 'no') "))
numstudents = 0
while response == 'yes':
  lastname = str(input("What is your last name? "))
  exam1 = int(input("What did you score on exam one? "))
  exam2 = int(input("What did you socre on exam two? "))
  avg = float((exam1+exam2)/2)
  numstudents = numstudents+1
  print(f"{lastname}'s average exam score is {avg:.1f}. Do you want to run this program again?")
  response = str(input("'yes' or 'no' "))

print(f"The number of students who input data was {numstudents}.")