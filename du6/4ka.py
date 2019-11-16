import cvxpy as cp
import numpy as np

def calculateProfit(gamma):
    x = cp.Variable(4)
    profitVector = np.matrix('0.07, 0.08, 0.09, 0.1')
    covarMatrix = np.matrix('1.1, -1.3, 2.5, -0.9; -1.3, 6.5, 0.7, -1.5; 2.5, 0.7, 11.1, 0.7; -0.9, -1.5, 0.7, 16.1')
    obj = cp.Maximize((profitVector * x) - gamma*cp.quad_form(x,covarMatrix))
    constraints = [cp.sum(x) == 1, x>=0]
    prob = cp.Problem(obj, constraints)
    prob.solve()
    print(x.value)

for gamma in np.arange(0,2.1,0.1):
    calculateProfit(gamma)

