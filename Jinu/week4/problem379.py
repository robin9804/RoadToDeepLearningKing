
nums = list(map(int,input().split()))
incre = []
last = []

for i in range(len(nums)):

    if nums[i] > nums[i-1]:

        if len(incre) != 0:
            incre.pop()

        incre.append(nums[i-1])
        incre.append(nums[i])

    elif nums[i] < nums[i-1]:
        last = incre
        incre = []

ans = last if len(incre) == 0 else incre
print(ans)