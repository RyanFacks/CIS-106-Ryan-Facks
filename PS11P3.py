f=open("data.txt","r")
lastn=[]
score=[]
lastname=f.readline()

while lastname !="":
  lastn.append(str(lastname).rstrip("\n"))
  s=float(f.readline())
  score.append(s)
  lastname=f.readline()
f.close()
l = len(lastname)

def display(lastname,score):
  for z in lastn,score:
    print (z)

def high(lastname,score):
  hvar=-1
  for x in (0,l,1):
    if float(score[x])>float(hvar):
      hindex=x
      hvar=score[x]

  print(lastn[hindex]," has the highest score of ", score[hindex])

def low(lastname,score):
  lvar=999
  for y in (l,0,-1):
    if float(score[y])<float(lvar):
      lindex=y
      lvar=score[y]
  print(lastn[lindex]," has the lowest score of ",score[lindex])

display(lastname,score)
high(lastname,score)
low(lastname,score)
