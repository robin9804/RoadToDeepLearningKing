# problem 228 + ex 220

matrix = [[1,2,3], [4,5,6], [7,8,9]]  # 2 차원 배열
print(matrix)
print(matrix[1])
print(matrix[0:2])
print(matrix[0][2])

import numpy as np 

def MinOrMax():
    mat = np.random.randint(1, 25, [5, 5])
    print(mat)
    if np.mean(mat) >= 12.5:
        return 'Big'
    else:
        return 'Small'

print(MinOrMax())