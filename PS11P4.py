f=open("data.txt","r")
pname=[]
bavg=[]
player=f.readline()
while player !="":
  pname.append(str(player).rstrip("\n"))
  b=float(f.readline())
  bavg.append(b)
  player=f.readline()
f.close()
l=len(pname)

def display (player,bavg):
  for z in pname,bavg:
    print(z)

def search(pname,player,bavg,playersearch):
  for y in range(0,9,1):
    if pname[y] in playersearch:
      sindex=y
      print(pname[sindex]," has a batting avg of ",bavg[sindex])

display(player,bavg)  

response = str(input("Do you want to search for a player? ('Yes' or 'no')"))
while "yes" in response.lower():
  playersearch=str(input("What player do you seek?"))
  search(pname,player,bavg,playersearch)
  response = str(input("Do you want to search another player? ('Yes' or 'No')"))



