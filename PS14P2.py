class car:
  def __init__(self,make,model,stickerprice):
    self.make=make
    self.model=model
    self.stickerprice=stickerprice
    self.discountprice=stickerprice*0.9

  def makemodel(self):
    return '{} {}'.format(self.make,self.model)

  def sprice(self):
    return self.stickerprice 
  def dprice(self):
    return self.discountprice

class sport(car):
  def sportwheel(car):
    car.stickerprice=car.stickerprice+1000
    return car.stickerprice
  def sportengine(car):
    car.stickerprice=car.stickerprice+3000
    return car.stickerprice
  def sportinterior(car):
    car.stickerprice=car.stickerprice+2000
    return car.stickerprice
  
  
  def updatedprice(car):
    car.updatedprice=car.sportwheel()
    car.updatedprice=car.sportengine()
    car.updatedprice=car.sportinterior()
    return car.updatedprice
  def updatedpricewdisc(car):
    car.updatedpricewdisc=car.updatedprice*0.9
    return car.updatedpricewdisc
    
car_1=car('Chrysler','200',30000)
car_2=car('Chevy','Cavalier',10000)
car_3=car('Toyota','Highlander',50000)
car_4=sport('Tesla','Model X',75000)

print(car_1.makemodel())
print("Sticker price is $",format(car_1.sprice(),".2f")," with a discount price of $",format(car_1.dprice(),".2f"))
print(car_2.makemodel())
print("Sticker price is $",format(car_2.sprice(),".2f")," with a discount price of $",format(car_2.dprice(),".2f"))
print(car_3.makemodel())
print("Sticker price is $",format(car_3.sprice(),".2f")," with a discount price of $",format(car_3.dprice(),".2f"))

print(car_4.makemodel())
print("Sticker price is $",format(car_4.sprice(),".2f")," with a discount price of $",format(car_4.dprice(),".2f"))

print("With options of sport wheels, sport engine, and sport interior for ",car_4.makemodel()," sticker price is $",format(car_4.updatedprice(),".2f")," with a discount price of $",format(car_4.updatedpricewdisc(),".2f"))