import cvxpy as cp
import numpy as np

b = cp.Variable(14)
#předměty seřazené jako v zadání 
w = [0.2,0.6,1.2,2.55,2.65,3.15,3.2,3.35,3.55,3.95,4.1,4.3,4.55,9]
u = [1.0,2.0,4.0,6.0,6.0,7.0,7.0,8.0,8.0,9.0,9.0,10.0,10.0,20.0]
obj = cp.Maximize(b*u)
constraints = [b>=0.0, b<=1.0, b*w<=10.0]



prob = cp.Problem(obj, constraints)
prob.solve()

# Print result.
print('Výsledná efektivita bude: ' + str(prob.value) + ' dz')
print('\nVektor b:')
print(np.round(b.value,2))

#výsledek je vlastně 
# 1x mapa
# 1x baterka
# 1x katana
# 1x rozladěná kytara
# 1x bowlingová koule
# 0.5x jarník
# celkem 25.88 dz
