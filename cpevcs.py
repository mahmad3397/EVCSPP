import time
import cplex
from input import *

start_time = time.time()
# ============================================================
# This file gives us a sample to use Cplex Python API to
# establish a Mixed Integer Linear Programming model and then solve it.
# The  problem displayed bellow is as:
#                  min z = cx
# ============================================================
# Input all the data and parameters here
'''
num_decision_var = 8
D=6
d = [[0,6,12,3,4,10,14,16],[6,0,6,9,10,4,8,10],[12,6,0,15,16,10,6,4],[3,9,15,0,1,7,11,13],[4,10,16,1,0,6,11,12],[10,4,10,7,6,0,4,6],[10,8,6,11,10,4,0,2],[16,10,4,13,12,6,2,0]]'''
con=[[0 for i in range(num_decision_var)] for j in range(num_decision_var)]

for i in range(num_decision_var):
 for j in range(num_decision_var):
  if(d[i][j]<=D and d[i][j]>0):
   con[i][j]=1
print(con)
E=[]
k=[]
for i in range(num_decision_var):
 for j in range(num_decision_var):
  if(con[i][j]==1):
   E.append("Y"+str(i)+str(j))
   k.append(j)
print(E)
#print(k)
'''
f = [1,1,1,1,1,1,1,1]#0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5
F = [1,1,1,1,1,1,1,1] # F values
c = [0.11, 0.41, 0.30, 0.08,0.2,0.5,0.35,0.4] #cost of constructions
x = ["x0", "x1", "x2", "x3","x4","x5","x6","x7"]'''

# ============================================================

# Establish the Linear Programming Model
myProblem = cplex.Cplex()

# Add objective function and set its sense
myProblem.variables.add(obj=c, names=x)
myProblem.objective.set_sense(myProblem.objective.sense.minimize)

# Add the decision variable

indices = myProblem.variables.add(names = E)
myProblem.variables.add(ub=[num_decision_var],names = ["x01"])
myProblem.variables.add(ub=[num_decision_var],names = ["y01"])

# Set the type of each variables
for i in range(num_decision_var):
 myProblem.variables.set_types(i, myProblem.variables.type.binary)
for i in range(len(x),myProblem.variables.get_num()):
 myProblem.variables.set_types(i, myProblem.variables.type.integer)

# Add constraints

#xj.fj>=Fi
for i in range(num_decision_var):
 rows = [[], []]
 for j in range(num_decision_var):
  rows[0].append(x[j])
  if(d[i][j]<=D):
   rows[1].append(f[j])
  else:
    rows[1].append(0)
 myProblem.linear_constraints.add(lin_expr=[rows], senses="G",
                                rhs=[F[i]])

#Yjk<=n.Xk
for i in range(len(E)):
 rows=[[E[i],k[i]],[1,-num_decision_var]]
 myProblem.linear_constraints.add(lin_expr=[rows], senses="L",
                                rhs=[0])

#sum(Yjk)=Xk+sum(Ykl)
for i in range(num_decision_var):
 rows=[[],[]]
 for j in range(num_decision_var):
  if(con[j][i]==1):
   rows[0].append("Y"+str(j)+str(i))
   rows[1].append(1)
 if(i==5):
  rows[0].append("y01")
  rows[1].append(1)
 rows[0].append("x"+str(i))
 rows[1].append(-1)
 for j in range(num_decision_var):
  if(con[i][j]==1):
   rows[0].append("Y"+str(i)+str(j))
   rows[1].append(-1)
 myProblem.linear_constraints.add(lin_expr=[rows], senses="E",
                                rhs=[0])

#X01+Y01=n
rows=[[],[]]
rows[0].append("x01")
rows[0].append("y01")
rows[1].append(1)
rows[1].append(1)
myProblem.linear_constraints.add(lin_expr=[rows], senses="E",
                                rhs=[num_decision_var])

#sum(xj)=y01
rows=[[],[]]
for i in range(len(x)):
 rows[0].append(x[i])
 rows[1].append(1)
rows[0].append("y01")
rows[1].append(-1)
myProblem.linear_constraints.add(lin_expr=[rows], senses="E",
                                rhs=[0])
#fixing i value to attach source node
rows=[[],[]]
rows[0].append("x0")
rows[1].append(1)
myProblem.linear_constraints.add(lin_expr=[rows], senses="E",
                                rhs=[1])

 
'''
#x0+y0=n
rows = [["x0", "x1", "x2", "x3","x4","x5","x6","x7"], [1.0, 1.0, 1.0, 1.0,1.0, 1.0, 1.0, 1.0]]
myProblem.linear_constraints.add(lin_expr=[rows], senses="E",
                                rhs=[n-x])
'''
'''
#Yjk<=n.Xk
for i in range(num_decision_var):
 rows = [["x0", "x1", "x2", "x3"], [0.0, 0.0, 0.0, 0.0]]
 for j in range(i):
  rows[1][j]=1/n
 rows[1][i]=1
 myProblem.linear_constraints.add(lin_expr=[rows], senses="G",
                                rhs=[1])

for i in range(num_decision_var):
 rows = [["x0", "x1", "x2", "x3"], [0.0, 0.0, 0.0, 0.0]]
 for j in range(i):
  rows[1][j]=1
 myProblem.linear_constraints.add(lin_expr=[rows], senses="L",
                                rhs=[n])


'''







''' Code to compute Yjk value; here in Yi, j=i-1 and k=i'''

#for i in range(num_decision_var):
 #rows = [["x0", "x1", "x2", "x3"], [0.0, 0.0, 0.0, 0.0]]
 #for j in range(i):
  #rows[1][j]=1
  

'''
# Add the decision variables and set their lower bound and upper bound (if necessary)
myProblem.variables.add(names= ["x"+str(i) for i in range(num_decision_var)])

# Set the type of each variables
for i in range(num_decision_var):
 myProblem.variables.set_types(i, myProblem.variables.type.binary)

#print(myProblem.variables.get_names(0))
#a=0
#for i in range(2):
 #a+=myProblem.variables.get_names(i)
#print(a)

# Add constraints
for i in range(num_constraints):
    myProblem.linear_constraints.add(
        lin_expr= [cplex.SparsePair(ind= [j for j in range(num_decision_var)], val= f[i])],
        rhs= [F[i]],
        names = ["c"+str(i)],
        senses = [constraint_type[i]]
    )

# Add objective function and set its sense
for i in range(num_decision_var):
    myProblem.objective.set_linear([(i, c[i])])
myProblem.objective.set_sense(myProblem.objective.sense.maximize)
'''
# Solve the model and print the answer
myProblem.solve()
res=myProblem.solution.get_values()
print(res)
print(x,end='')
print(E,end='')
print(",[x01,y01]")
cost=0
for i in range(len(x)):
 cost+=c[i]*res[i]
print("Total cost is ",end="")
print(cost) 

end_time = time.time()
print("Computation time (s) ", end="")
print(end_time-start_time)
