arr = input('Enter the numbers : ').split()
n = len(arr)

for i in range(len(arr)):
    for j in range(len(arr)):
        ind = j + i
        if ind > n - 1:
            ind -= n

        print(arr[ind], end=' ')
    print()