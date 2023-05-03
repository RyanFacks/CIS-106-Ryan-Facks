class employee:
  def __init__(self,first,last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@compay.com'
    self.bonusrate = pay*1.10

  def fullname(self):
    return '{} {}'.format(self.first,self.last)

  def emailaddress(self):
    return self.email

  def bonus(self):
    return self.bonusrate

class manager(employee):
  def managerbonus(employee):
    employee.pay=employee.pay*1.4
    return employee.pay
  

emp_1 = employee('Frank', 'Alvino',80000)
emp_2 = employee('Ryan','Facks',75000)
emp_3 = employee('Larry','Voyles',90000)

emp_4 = manager('Lisa','Blaylock',100000)

print(emp_1.fullname())
print(emp_1.emailaddress())
print("$",format(emp_1.bonus(),".2f")," is ",emp_1.fullname(), "'s salary with a 10% bonus.")
print(emp_2.fullname())
print(emp_2.emailaddress())
print("$",format(emp_2.bonus(),".2f")," is ",emp_2.fullname(), "'s salary with a 10% bonus.")
print(emp_3.fullname())
print(emp_3.emailaddress())
print("$",format(emp_3.bonus(),".2f"), " is ",emp_3.fullname(), "'s salary with a 10% bonus.")

print(emp_4.fullname())
print(emp_4.emailaddress())
print("$",format(emp_4.managerbonus(),".2f"), " is ",emp_4.fullname(), "'s salary with a 40% bonus.")