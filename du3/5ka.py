import cvxpy as cp
import numpy as np

def expectedValue(x):
    value = 0
    for i in range(1,100):
        value = value + i*x[i-1]
    return value


# Entropy maximization.
x = cp.Variable(99)
obj = cp.Maximize(cp.sum(cp.entr(x)))
constraints = [expectedValue(x) == 31, x>=0, cp.sum(x) == 1]
prob = cp.Problem(obj, constraints)
prob.solve()

# Print result.
print("\nThe optimal value is:", prob.value)
print('\nThe optimal solution is:')
print(x.value)
#p_i are x_i