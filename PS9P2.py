def sqft(length,width,height):
  sqft=(2*length*width)+(2*length*height)+(2*width*height)
  return sqft

response = str(input("Do you want to run this program? ('Yes' or 'No')" ))
while response.lower() == "yes":
  length = int(input("What is the length of the room? "))
  width = int(input("What is the width of the room? "))
  height = int(input("What is the height of the room?" ))
  paint = (sqft(length,width,height))//50
  remainder = (sqft(length,width,height))%50
  
  if remainder > 0:
    print(f"You will need {paint} gallons of paint to cover the room.")
    print(f"You will need an a partial gallon of paint for {remainder} square feet.")
  else:
    print(f"You will need {paint} gallons of paint to cover the room.")
  response = str(input("Do you want to run this program? ('Yes' or 'No')" ))

print("Now exiting program")
exit()