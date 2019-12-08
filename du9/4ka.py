import cvxpy as cp
import numpy as np

##worst case opt for P1 (P)
t = cp.Variable(1)
p = cp.Variable(8)
obj = cp.Maximize(t)
constraints = [p >= 0, cp.sum(p)==1, 
t <= -p[0]+p[1]+p[2]+p[3]-p[4]+p[5]+p[6]+p[7],
t <= p[0]-p[1]+p[2]+p[3]-p[4]-p[5]+p[6]+p[7],
t <= p[0]+p[1]-p[2]+p[3]+p[4]-p[5]-p[6]+p[7],
t <= p[0]+p[1]+p[2]+p[3]+p[4]+p[5]-p[6]+p[7],
t <= -p[0]+p[1]+p[2]-p[3]+p[4]+p[5]+p[6]+p[7],
t <= p[0]-p[1]+p[2]-p[3]+p[4]+p[5]+p[6]-p[7],
t <= p[0]+p[1]-p[2]+p[3]+p[4]+p[5]+p[6]-p[7],
]

prob = cp.Problem(obj, constraints)
prob.solve()

# Print result.
print("Vysledek obj funkce:", prob.value)
print("P:", p.value)
print("const :", constraints[0].dual_value)
print("const :", constraints[1].dual_value)
print("const :", constraints[2].dual_value)
print("const :", constraints[3].dual_value)
print("const :", constraints[4].dual_value)
print("const :", constraints[5].dual_value)
print("const :", constraints[6].dual_value)
print("const :", constraints[7].dual_value)
print("const :", constraints[8].dual_value)



##worst case opt for P2 (Q)
t = cp.Variable(1)
p = cp.Variable(7)
obj = cp.Maximize(t)
constraints = [p >= 0, cp.sum(p)==1, 
t <= -p[0]+p[1]+p[2]+p[3]-p[4]+p[5]+p[6],
t <= p[0]-p[1]+p[2]+p[3]+p[4]-p[5]+p[6],
t <= p[0]+p[1]-p[2]+p[3]+p[4]+p[5]-p[6],
t <= p[0]+p[1]+p[2]+p[3]-p[4]-p[5]+p[6],
t <= -p[0]-p[1]+p[2]+p[3]+p[4]+p[5]+p[6],
t <= p[0]-p[1]-p[2]+p[3]+p[4]+p[5]+p[6],
t <= p[0]+p[1]-p[2]-p[3]+p[4]+p[5]+p[6],
t <= p[0]+p[1]+p[2]+p[3]+p[4]-p[5]-p[6],
]

prob = cp.Problem(obj, constraints)
prob.solve()

# Print result.
print("Vysledek obj funkce:", prob.value)
print("Q:", p.value)