import time
from ap import *
from input import *

start_time = time.time()

x=[]
for i in range(num_decision_var):
 x.append(1)
'''
f=[1,1,1,1,1,1,1,1] #charging capicity
F=[1,1,1,1,1,1,1,1] #Demand
c=[0.11,0.41,0.30,0.08,0.2,0.5,0.35,0.4] #cost of constructions
d = [[0,6,12,3,4,10,14,16],[6,0,6,9,10,4,8,10],[12,6,0,15,16,10,6,4],[3,9,15,0,1,7,11,13],[4,10,16,1,0,6,11,12],[10,4,10,7,6,0,4,6],[10,8,6,11,10,4,0,2],[16,10,4,13,12,6,2,0]] #distance vector
D=6'''
while True:
 g1=Graph(len(x))
 #print(x)
 for i in range(len(x)):
  if(x[i]==1):
   for j in range(len(x)):
    if(x[j]==1 and d[i][j]<=D and d[i][j]>0):
     g1.addEdge(i, j)
 N=[]
 g1.AP(N,x) 
 #print(N)
 temp=x[:]
 flag=0
 while True:
  if(flag==1 or len(N)==0):
   break
  max=0
  for i in range(len(N)):
   if(c[N[i]]>max):
    max=c[N[i]]
    j=N[i]
  #print(j)
  temp[j]=0
  for i in range(len(x)):
   total=0
   p=0
   for k in range(len(x)):
    if(d[i][k]<=D):
     total+=f[k]*temp[k]
   if(total>=F[i]):
    p=1
   else:
    p=0
    break
  if(p==1):
   x=temp[:]
   #print(x)
   flag=1
  else:
   temp[j]=1
   N.remove(j)
 
 #print(N)
 #print(x)
 if(len(N)==0):
  break
print(x)
cost=0
for i in range(len(x)):
 cost+=c[i]*x[i]
print("Total cost is ",end="")
print(cost)
end_time = time.time()
print("Computation time (s) ", end="")
print(end_time-start_time)
 

