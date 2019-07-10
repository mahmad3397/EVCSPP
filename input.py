# Input all the data and parameters here
#num_decision_var = 8
f1=open('text8.txt','r')
f1_contents=f1.readline()
num_decision_var=int(f1_contents)
#print(num_decision_var)

#D=20
f1_contents=f1.readline()
D=int(f1_contents)
#print(D)

#f = [1,1,1,1]
f=[]
f1_contents=f1.readline()
newletter=''
for letter in f1_contents:
 
 if(letter!=" " and letter!='\n'):
  newletter+=letter
 else:
  i=float(newletter)
  f.append(i)
  newletter=''
#print(f)

#F = [1,1,1,1] # F values
F=[]
f1_contents=f1.readline()
newletter=''
for letter in f1_contents:
 
 if(letter!=" " and letter!='\n'):
  newletter+=letter
 else:
  i=int(newletter)
  F.append(i)
  newletter=''
#print(F)

#c = [0.11,0.41,0.30,0.08] #cost of constructions
c=[]
f1_contents=f1.readline()
newletter=''
for letter in f1_contents:
 
 if(letter!=" " and letter!='\n'):
  newletter+=letter
 else:
  i=float(newletter)
  c.append(i)
  newletter=''
#print(c)

#x = ["x0", "x1", "x2", "x3"]
x=[]
f1_contents=f1.readline()
newletter=''
for letter in f1_contents:
 
 if(letter!=" " and letter!='\n'):
  newletter+=letter
 else:
  x.append(newletter)
  newletter=''
#print(x)

#d = [[0,15,23,39],[15,0,8,24],[23,8,0,16],[39,24,16,0]]
d = []
# Append empty lists in first four indexes.
for i in range(len(x)):
 d.append([])
i=0
while True:
 f1_contents=f1.readline()
 if(f1_contents==''):
  break
 newletter=''
 for letter in f1_contents:
 
  if(letter!=" " and letter!='\n'):
   newletter+=letter
  else:
   j=int(newletter)
   d[i].append(j)
   newletter=""
 i=i+1
#print(d)
