class student:
  def __init__(self,first,last,dcode,credits):
    self.first = first
    self.last = last
    self.dcode = dcode
    if "I" in dcode:
      self.tuition = credits*250.0
    elif "O" in dcode:
      self.tuition = credits*500.0

  def fullname(self):
    return '{} {}'.format(self.first,self.last)

  def tuitionowed(self):
    return self.tuition

stu_1=student('Frank','Alvino','O',10)
stu_2=student('Ryan','Facks','O',15)
stu_3=student('Larry','Voyles','I',10)

print("Student: ",stu_1.fullname())
print(stu_1.fullname(), " owes $",format(stu_1.tuitionowed(),".2f")," in tuition.")
print("Student: ",stu_2.fullname())
print(stu_2.fullname(), " owes $",format(stu_2.tuitionowed(),".2f")," in tuition.")
print("Student: ",stu_3.fullname())
print(stu_3.fullname(), " owes $",format(stu_3.tuitionowed(),".2f")," in tuition.")