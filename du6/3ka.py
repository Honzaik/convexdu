import cvxpy as cp
import numpy as np


y = cp.Variable(7) #y_1 = log(v_1), y_2 = log(v_2), .., y_4 = log(v_4), y_5 = log(lambda), y_6 = log(c), y_7 = log(d)
obj = cp.Minimize(cp.exp(y[4]))
constraints = [y>=0,
0.5*cp.exp(-y[4]-y[5])+0.7*cp.exp(-y[4]-y[5]-y[0]+y[1]-y[6])+0.5*cp.exp(-y[4]+y[5]-y[6]-y[0]+y[2])+0.4*cp.exp(-y[4]-y[0]+y[5]+y[6]+y[3])<=1,
0.7*cp.exp(-y[4]-y[1]+y[0]) <= 1,
0.7*cp.exp(-y[4]-y[2]+y[1]) <= 1,
0.7*cp.exp(-y[4]-y[3]+y[2]) <= 1
]
prob = cp.Problem(obj, constraints)
prob.solve()
print(y.value)
print('l: ' + str(np.exp(y[4].value))) #lambda
print('c: ' + str(np.exp(y[5].value))) #c
print('d: ' + str(np.exp(y[6].value))) #d
