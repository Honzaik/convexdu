import cvxpy as cp
import numpy as np
import csv

matrix = []
smoulove = []
with open('mining.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            
        else:
            smoulove.append(row[0])
            matrix.append(row[1:])

        line_count += 1

b = matrix[len(matrix)-1]
matrix = matrix[:len(matrix)-1]
smoulove = smoulove[:len(smoulove)-1]
print(np.matrix(matrix))
print(smoulove)
n = len(smoulove)

x = cp.Variable(n)
cost = cp.sum_squares(matrix*x - b)
prob = cp.Problem(cp.Minimize(cost))
prob.solve()

# Print result.
print("\nThe optimal value is", prob.value)
print("The optimal x is")
print(x.value)
print("The norm of the residual is ", cp.norm(matrix*x - b, p=2).value)