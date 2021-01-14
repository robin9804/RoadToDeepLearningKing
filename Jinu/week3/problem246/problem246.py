print("Enter the number : ", end = ' ')
num = int(input())

i = 0
j = 0
nums = [[1 for i in range(num)] for j in range(num)]

for i in range(num):
    for j in range(num):
        if (i % 2) == 0:
            nums[i][j] = num * i + j + 1
        elif (i%2) == 1:
            nums[i][-j-1] = num * i + j + 1

    print(nums[i])