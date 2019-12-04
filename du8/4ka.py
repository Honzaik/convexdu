import cvxpy as cp
import numpy as np

def reseni(vahy):
    deltas = cp.Variable(99)
    ys = cp.Variable(101)
    vs = cp.Variable(100)
    s = cp.Variable(1)
    obj = cp.Minimize(vahy[0]*cp.sum_squares(deltas)-vahy[1]*s)
    constraints = []

    for i in range(1,101):
        constraints.append(ys[i]==ys[i-1]+0.1*vs[i-1])

    for i in range(1,100):
        constraints.append(vs[i]==vs[i-1]+deltas[i-1])

    #bariery
    ais = [1, 2, 5, -1, -2, 3, 10, 12, 8, 0]
    bis = [2, 3, 6, 0, -1.5, 7, 11, 13, 9, 1]

    for i in range(1,11):
        constraints.append(ys[i*10] <= bis[i-1])
        constraints.append(-ys[i*10] <= -(ais[i-1]))
        constraints.append(s <= ys[i*10]-ais[i-1])
        constraints.append(s <= bis[i-1]-ys[i*10])

    constraints.append(vs[0]==0)
    constraints.append(ys[0]==0)
    constraints.append(s >= 0)


    prob = cp.Problem(obj, constraints)
    prob.solve()

    # Print result.
    print("Vysledek obj funkce:", prob.value)
    print("Min vzdalenost:", s[0].value)
    print("Palivo:", cp.sum_squares(deltas).value)
    print('Hodnoty y v bodech, kde jsou bariery:')
    for i in range(1,11):
        print(ys[i*10].value)

    print('\nVektor delt:')
    print(deltas.value)


vahy =[1,10]
reseni(vahy)

vahy =[1,20]
reseni(vahy)

vahy =[20,30]
reseni(vahy)