import cvxpy as cp
import numpy as np

#verze b)
deltas = cp.Variable(99)
ys = cp.Variable(101)
vs = cp.Variable(100)
obj = cp.Minimize(cp.sum_squares(deltas))
constraints = []

for i in range(1,101):
    constraints.append(ys[i]==ys[i-1]+0.1*vs[i-1])

for i in range(1,100):
    constraints.append(vs[i]==vs[i-1]+deltas[i-1])

#body barier
ais = [5, 7, 6, 8, 4, 9, 5, 1, 5, 0]
bis = [6, 8, 8, 9, 9, 10, 8, 3, 6, 1]

for i in range(1,11):
    constraints.append(ys[i*10] <= bis[i-1])
    constraints.append(-ys[i*10] <= -(ais[i-1]))

constraints.append(vs[0]==0)
constraints.append(ys[0]==0)


prob = cp.Problem(obj, constraints)
prob.solve()

# Print result.
print('-----Nebezpečná verze b)-------')
print("\nSpotřebujeme paliva (nebezpečná verze):", prob.value)
unsafePalivo = prob.value
print('\nVektor delt:')
print(deltas.value)
print('Hodnoty y v bodech, kde jsou bariery:')
for i in range(1,11):
    print(ys[i*10].value)


#verze d)
deltas = cp.Variable(99)
ys = cp.Variable(101)
vs = cp.Variable(100)
obj = cp.Minimize(cp.sum_squares(deltas))
constraints = []

for i in range(1,101):
    constraints.append(ys[i]==ys[i-1]+0.1*vs[i-1])

for i in range(1,100):
    constraints.append(vs[i]==vs[i-1]+deltas[i-1])

for i in range(1,11):
    constraints.append(ys[i*10] <= bis[i-1] - 0.01)
    constraints.append(-ys[i*10] <= -(ais[i-1]+0.01))

constraints.append(vs[0]==0)
constraints.append(ys[0]==0)


prob = cp.Problem(obj, constraints)
prob.solve()

# Print result.
print('-----Bezpečná verze b)-------')
print("\nSpotřebujeme paliva (bezpečná verze):", prob.value)
print('\nVektor delt:')
print(deltas.value)
print('Hodnoty y v bodech, kde jsou bariery:')
for i in range(1,11):
    print(ys[i*10].value)


print('V bezpečnější verzi spotřebujeme o ' + str(prob.value - unsafePalivo) + ' paliva navíc.')
