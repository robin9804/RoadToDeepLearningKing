
A = [[1,2], [2,3]]
B = [[3,4], [5,6]]

def sumMatrix(list1, list2):

    len_ax = len(list1[0])
    len_bx = len(list2[0])

    len_ay = len(list1)
    len_by = len(list2)

    answer = [[1 for i in range(len_ax)] for j in range(len_ay)]

    for m in range(len_ax):
        for n in range(len_ay):

            answer[m][n] = list1[m][n] + list2[m][n]

    return answer

print(sumMatrix(A,B))
