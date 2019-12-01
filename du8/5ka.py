import cvxpy as cp
import numpy as np

##worst case opt for P1 (P)
t = cp.Variable(1)
p = cp.Variable(3)
obj = cp.Maximize(t)
constraints = [p >= 0, cp.sum(p)==1, t<= 2*p[1]+3*p[2], t <= p[0]+3*p[2], t<=p[0]+2*p[1]]

prob = cp.Problem(obj, constraints)
prob.solve()

# Print result.
print("Vysledek obj funkce:", prob.value)
print("P:", p.value)

##worst case opt for P2 (Q)
t = cp.Variable(1)
q = cp.Variable(3)
obj = cp.Maximize(t)
constraints = [q >= 0, cp.sum(q)==1, t<= q[1]+q[2], t <= 2*q[0]+2*q[2], t<=3*q[0]+3*q[1]]

prob = cp.Problem(obj, constraints)
prob.solve()

# Print result.
print("Vysledek obj funkce:", prob.value)
print("Q:", q.value)