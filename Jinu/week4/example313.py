
import itertools

nums = [1,2]
nums_list = [nums] * 3
allcase1 = itertools.product(nums, nums, nums)
for i in allcase1:
    print(i, end = ' ')
print()

allcase2 = itertools.product(*nums_list)
for i in allcase2:
    print(i, end = ' ')
