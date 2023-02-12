FirstExam = int(input("What did you score on your first exam? "))
SecondExam = int(input("What did you score on your second exam? "))

Weighted1 = float(FirstExam * 0.6)
Weighted2 = float(SecondExam * 0.4)
TotalScore = Weighted1 + Weighted2

print("After weights are applied, your final grade is ", TotalScore) 

input("Please press enter to exit.")