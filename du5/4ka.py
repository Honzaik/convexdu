import cvxpy as cp
import numpy as np



def existsAtLeast(alpha):
    A = np.matrix('-1.0 0.0 -3.0 0.0 5.0; -1.0 0.0 0.0 -1.0 2.0; 0.0, 0.0, 10.0, 0.0, -2.0; 3.0, -1.0, 0.0, 1.0, 0.0; -1.0, 1.0, -3.0, 1.0, -3.0')
    B = np.matrix('1.0 0.0 3.0 0.0 0.0; 1.0 0.0 0.0 1.0 0.0; 0.0, 0.0, 0.0, 0.0, 2.0; 0.0, 1.0, 0.0, 0.0, 0.0; 1.0, 0.0, 3.0, 0.0, 3.0')
    x1 = cp.Variable(5) #x+
    x2 = cp.Variable(5) #x
    t = cp.Variable(1)
    obj = cp.Minimize(0)
    constraints = [x1>=0, x2>=0, A*x2 <= B*x1, x1-x2*alpha >= 0, sum(x2) == 1]
    prob = cp.Problem(obj, constraints)
    prob.solve()
    print(x1.value)
    print(x2.value)
    print(prob.value)
    if prob.value == np.inf:
        return False
    else:
        print(min(x1.value/x2.value))
        return True

def existsLessThan(alpha):
    A = np.matrix('-1.0 0.0 -3.0 0.0 5.0; -1.0 0.0 0.0 -1.0 2.0; 0.0, 0.0, 10.0, 0.0, -2.0; 3.0, -1.0, 0.0, 1.0, 0.0; -1.0, 1.0, -3.0, 1.0, -3.0')
    B = np.matrix('1.0 0.0 3.0 0.0 0.0; 1.0 0.0 0.0 1.0 0.0; 0.0, 0.0, 0.0, 0.0, 2.0; 0.0, 1.0, 0.0, 0.0, 0.0; 1.0, 0.0, 3.0, 0.0, 3.0')
    x1 = cp.Variable(5) #x+
    x2 = cp.Variable(5) #x
    t = cp.Variable(1)
    obj = cp.Minimize(0)
    constraints = [x1>=0, x2>=0, A*x2 <= B*x1, x1-x2*alpha <= 0, sum(x2) == 1]
    prob = cp.Problem(obj, constraints)
    prob.solve()
    print(x1.value)
    print(x2.value)
    print(prob.value)
    if prob.value == np.inf:
        return False
    else:
        print(min(x1.value/x2.value))
        return True


print(existsAtLeast(90))
print(existsLessThan(30))