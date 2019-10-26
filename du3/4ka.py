import cvxpy as cp
import numpy as np
import csv

matrix = []
trpaslici = []
with open('mining.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        else:
            trpaslici.append(row[0])
            matrix.append(row[1:])
            line_count += 1

b = matrix[len(matrix)-1]
matrix = matrix[:len(matrix)-1]
trpaslici = trpaslici[:len(trpaslici)-1]
n = len(trpaslici)
x = cp.Variable(n)
cost = cp.sum_squares(matrix*x - b)
prob = cp.Problem(cp.Minimize(cost))
prob.solve()

for i in range(len(trpaslici)):
    print(trpaslici[i] + ' vytěží průměrně ' + str(x.value[i]) + ' zlata za den')

#vektor je x.value