import math

i = 0
j = 0

nums = [[0 for i in range(2)] for j in range(3)]

for i in range(3):
    for j in range(2):

        print(i+1, '열', j+1, '행 수 입력 : ')
        nums[i][j] = int(input())

sum = 0


for i in range(3):

    print(nums[int(i)])


    for j in range(2):
        sum = sum + int(nums[i][j])

print('가로 평균 : {} {} {}'.format(math.floor((int(nums[0][0])+int(nums[0][1]))/2), 
                                math.floor((int(nums[1][0])+int(nums[1][1]))/2), math.floor((int(nums[2][0])+int(nums[2][1]))/2)))
print('세로 평균 : {} {}'.format(math.floor(int(nums[0][0])+int(nums[1][0]) + int(nums[2][0])/3), math.floor((int(nums[1][1])+int(nums[1][1])+int(nums[2][1]))/3)))
print('전체 평균 : ', math.floor(sum/6))