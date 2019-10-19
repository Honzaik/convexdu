import cvxpy as cp
import numpy as np

x = cp.Variable()
m1 = cp.Variable()
m2 = cp.Variable()
m3 = cp.Variable()
m4 = cp.Variable()
m5 = cp.Variable()
m6 = cp.Variable()
m7 = cp.Variable()
m8 = cp.Variable()
m9 = cp.Variable()
m10 = cp.Variable()

mesice = [80,50,200,70,60,20,300,150,180,100]
prob = cp.Problem(cp.Minimize(8*x+15*(1/10)*(m1+m2+m3+m4+m5+m6+m7+m8+m9+m10)), [x>=0,m1>=0,
    m2>=0,
    m3>=0,
    m4>=0,
    m5>=0,
    m6>=0,
    m7>=0,
    m8>=0,
    m9>=0,
    m10>=0,
    m1>=80-x,
    m2>=50-x,
    m3>=200-x,
    m4>=70-x,
    m5>=60-x,
    m6>=20-x,
    m7>=300-x,
    m8>=150-x,
    m9>=180-x,
    m10>=100-x,
    ])

prob.solve()

print("\nThe optimal value is", prob.value)
print("A solution x is")
print(x.value)