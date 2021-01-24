# problem 348

def sum_mat(a, b):
    if len(a) != len(b):
        raise Exception('Wrong number error')
    for i in range(len(a)):
        for j in range(len(a[i])):
            b[i][j] += a[i][j]
    return b


a = [[1,2],[3, 4]]
b = [[0, 1], [2, 3]]
print(len(a))
print(sum_mat(a, b))
