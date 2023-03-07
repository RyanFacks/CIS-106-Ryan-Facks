f=open("district.txt","r")
lastname=str(f.readline().rstrip('\n'))
count = 0
sumtuition = 0

while lastname!="":
  district=str(f.readline())
  credits=int(f.readline())
  if district == "In":
    creditprice = 250
  else:
    creditprice = 500
  tuition=credits*creditprice
  count = count+1
  print(f"Student Name: {lastname}")
  print(f"Credits taken: {credits}")
  print(f"Tuition Due: ${tuition:.2f} \n")
  sumtuition=sumtuition+tuition
  lastname=str(f.readline())

f.close()

print(f"Number of students: {count}")
print(f"The sum of all the tuition is ${sumtuition:.2f}")