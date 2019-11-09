import cvxpy as cp
import numpy as np


x1 = cp.Variable(5) #x+
x2 = cp.Variable(5) #x
t = cp.Variable(1)
alfa = 9000
A = np.matrix('-1.0 0.0 -3.0 0.0 5.0; -1.0 0.0 0.0 -1.0 2.0; 0.0, 0.0, 10.0, 0.0, -2.0; 3.0, -1.0, 0.0, 1.0, 0.0; -1.0, 1.0, -3.0, 1.0, -3.0');
B = np.matrix('1.0 0.0 3.0 0.0 0.0; 1.0 0.0 0.0 1.0 0.0; 0.0, 0.0, 0.0, 0.0, 2.0; 0.0, 1.0, 0.0, 0.0, 0.0; 1.0, 0.0, 3.0, 0.0, 3.0');

obj = cp.Minimize(0)
constraints = [x1>=0, x2>=1, A*x2 <= B*x1, x1-x2*alfa >= 0]



prob = cp.Problem(obj, constraints)
prob.solve(max_iter=10000000)

# Print result.
print(prob.value)
print(x1.value)
print(x2.value)


x1 = cp.Variable(5) #x+
x2 = cp.Variable(5) #x
t = cp.Variable(1)
A = np.matrix('-1.0 0.0 -3.0 0.0 5.0; -1.0 0.0 0.0 -1.0 2.0; 0.0, 0.0, 10.0, 0.0, -2.0; 3.0, -1.0, 0.0, 1.0, 0.0; -1.0, 1.0, -3.0, 1.0, -3.0');
B = np.matrix('1.0 0.0 3.0 0.0 0.0; 1.0 0.0 0.0 1.0 0.0; 0.0, 0.0, 0.0, 0.0, 2.0; 0.0, 1.0, 0.0, 0.0, 0.0; 1.0, 0.0, 3.0, 0.0, 3.0');

obj = cp.Maximize(t)
constraints = [x1>=0, x2>=1, A*x2 <= B*x1, x1-x2*alfa == t, t >= -5000, t<= 5000]



prob = cp.Problem(obj, constraints)
prob.solve(max_iter=10000000)

# Print result.
print(prob.value)
print(x1.value)
print(x2.value)



