def d1 (dlist):
  x=int(input("How many items are in the list? "))
  for x in range(0,x,1):
    i=int(input("Please enter a number "))
    dlist.append(i)
  return dlist

def d2(dlist):
  dlist.insert(0,99)
  
def d3(dlist):
  dlist[0]=100

def d4(dlist):
  dlist.extend(dlist2)

def d5(dlist):
  dlist.remove(800)

def d6(dlist):
  dlist.remove(dlist[2])

def display(dlist):
  for z in dlist:
    print(z)

def isgradea(grades):
  print("There are " ,grades.count("A")," A grades.")

def whereb(grades):
  print("The first 'B' is at position ",grades.index("B"))

def ferror(grades):
  print("There are ",grades.count("F")," F grades in the list.")

def d11(grades):
  dlist2.clear()

def playersort(players):
  players.sort()
  for i in players:
    print(i)

def copyplayers(players,players2):
  y=players.copy()
  players2.append(y)
  return players2
  for y in players2:
    print(y)

def backwards(players,players2):
  players.sort()
  for t in players:
    print(t)
  z=players.copy()
  players2.append(z)
  w=reversed(players)
  print(list(w))


  
dlist=[]
dlist2=[500,600,700,800,900]
#dlist=d1 (dlist)

#d11(dlist)
#d2(dlist)
#d3(dlist)
#d4(dlist)
#d5(dlist)
#d6(dlist)

#display(dlist)

grades = ["A","B","C","A","A","C"]
#isgradea(grades)
#whereb(grades)
#ferror(grades)

players=["Rizzo","Davis","Baez","Happ","Bryan"]
players2=[]

#playersort(players)
#copyplayers(players,players2)
backwards(players,players2)