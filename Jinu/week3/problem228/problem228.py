
import random

i = 0
j = 0
nums = [[0 for i in range(5)] for i in range(5)]
sum = 0

for i in range(5):

    
    for j in range(5):

        nums[i][j] = random.randrange(1,25)
        sum = sum + int(nums[i][j])

    print(nums[i])

aver = 'Big' if ((sum / 25) > 12.5) else 'Small'
print(aver)
