lname=["Albert","Barth","Charlie","Dean","Effren","Facks","Greg","Hector","Isabel","Jackson"]
scores=[100.0,98.0,96.0,94.0,92.0,90.0,88.0,86.0,84.0,82.0]
def exams(lname,scores):
  for x in range(0,10,1):
    print(lname[x], " scored ", scores[x])
exams(lname,scores)