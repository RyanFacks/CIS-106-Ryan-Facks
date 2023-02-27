response = str(input("Do you want to run this program? ('yes' or 'no') "))
numemployee = 0
sumofgross = 0

while response == 'yes':
  lastname = str(input("What is your last name? "))
  hourswork = int(input("How  many hours did you work? "))
  payrate = float(input("What is your payrate? "))
  if hourswork > 40:
    grosspay = 40 * payrate
    overtime = (hourswork-40)*(payrate*1.5)
    grosspay = grosspay + overtime
  else:
    grosspay = hourswork*payrate
  print(f"{lastname} your gross pay is ${grosspay:.2f}")
  numemployee = numemployee+1
  sumofgross = sumofgross + grosspay
  response = str(input("Do you want to run this program again?  ('yes' or 'no') "))

avgpay = sumofgross/numemployee

print(f"{numemployee} employees ran the program.  The sum of all the gross pays entered is ${sumofgross:.2f} and the average pay is ${avgpay:.2f}.")