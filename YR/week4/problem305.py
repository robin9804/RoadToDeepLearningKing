# problem 305

arr = [1, 2, 3, 4, 5]

arr2 = range(1, 6)

answer = 0
for i in arr:
    arr2 = [1, 2, 3, 4, 5]
    arr2.remove(i)
    for j in arr2:
        arr3 = arr2.copy()
        arr3.remove(j)
        for k in arr3:
            print(i, j, k)
            answer += 1

print(answer, ' is answer')