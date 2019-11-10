import cvxpy as cp
import numpy as np



def existsAtLeast(alpha):
    A = np.matrix('0, 0, 0, 0.0, 5.0; 0.0, 0.0, 0.0, 0.0, 2.0; 0.0, 0.0, 10.0, 0.0, 0.0; 3.0, 0.0, 0.0, 1.0, 0.0; 0.0, 1.0, 0.0, 1.0, 0.0')
    B = np.matrix('1.0, 0.0, 3.0, 0.0, 0.0; 1.0, 0.0, 0.0, 1.0, 0.0; 0.0, 0.0, 0.0, 0.0, 2.0; 0.0, 1.0, 0.0, 0.0, 0.0; 1.0, 0.0, 3.0, 0.0, 3.0')
    xplus = cp.Variable(5) #x+
    x = cp.Variable(5) #x
    t = cp.Variable(1)
    obj = cp.Minimize(0)
    constraints = [x>=0, xplus>=0, B*xplus <= A*x, xplus-x*alpha >= 0, cp.sum(x) == 1]
    prob = cp.Problem(obj, constraints)
    prob.solve()
    #print(xplus.value)
    #print(x.value)
    #print(prob.value)
    if prob.value == np.inf:
        return False
    else:
        #print(min(xplus.value/x.value))
        return True

leftBound = 0.01
rightBound = 100.0

while rightBound - leftBound > 0.005:
    middle = (rightBound + leftBound)/2
    if existsAtLeast(middle) == True:
        leftBound = middle
    else:
        rightBound = middle

print(rightBound)
print(leftBound)
print('Opt. výsledek approx: ' + str((rightBound+leftBound)/2))