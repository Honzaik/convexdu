import cvxpy as cp
import numpy as np



def existsAtLeast(alpha):
    A = np.matrix('-1.0, 0.0, -3.0, 0.0, 5.0; -1.0, 0.0, 0.0, -1.0, 2.0; 0.0, 0.0, 10.0, 0.0, -2.0; 3.0, -1.0, 0.0, 1.0, 0.0; -1.0, 1.0, -3.0, 1.0, -3.0')
    A = np.matrix('0, 0, 0, 0.0, 5.0; 0.0, 0.0, 0.0, 0.0, 2.0; 0.0, 0.0, 10.0, 0.0, 0.0; 3.0, 0.0, 0.0, 1.0, 0.0; 0.0, 1.0, 0.0, 1.0, 0.0')
    B = np.matrix('1.0, 0.0, 3.0, 0.0, 0.0; 1.0, 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 0.0, 2.0; 0.0, 1.0, 0.0, 0.0, 0.0; 1.0, 0.0, 3.0, 0.0, 3.0')
    xplus = cp.Variable(5) #x+
    x = cp.Variable(5) #x
    t = cp.Variable(1)
    obj = cp.Minimize(0)
    constraints = [x>=0, xplus>=0, B*xplus <= A*x, xplus-x*alpha >= 0, cp.sum(x) == 1]
    prob = cp.Problem(obj, constraints)
    prob.solve()
    print(xplus.value)
    print(x.value)
    print(prob.value)
    if prob.value == np.inf:
        return False
    else:
        print(min(xplus.value/x.value))
        return True

def existsLessThan(alpha):
    A = np.matrix('-1.0 0.0 -3.0 0.0 5.0; -1.0 0.0 0.0 -1.0 2.0; 0.0, 0.0, 10.0, 0.0, -2.0; 3.0, -1.0, 0.0, 1.0, 0.0; -1.0, 1.0, -3.0, 1.0, -3.0')
    B = np.matrix('1.0 0.0 3.0 0.0 0.0; 1.0 0.0 0.0 1.0 0.0; 0.0, 0.0, 0.0, 0.0, 2.0; 0.0, 1.0, 0.0, 0.0, 0.0; 1.0, 0.0, 3.0, 0.0, 3.0')
    xplus = cp.Variable(5) #x+
    x = cp.Variable(5) #x
    t = cp.Variable(1)
    obj = cp.Minimize(0)
    constraints = [x>=0, xplus>=0, B*xplus <= A*x, xplus-x*alpha <= 0]
    prob = cp.Problem(obj, constraints)
    prob.solve()
    print(xplus.value)
    print(x.value)
    print(prob.value)
    if prob.value == np.inf:
        return False
    else:
        print(min(xplus.value/x.value))
        return True


print(existsAtLeast(1.05))
#print(existsLessThan(30))