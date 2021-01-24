# example 313

import itertools

nums = [1, 2]
nums_list = [nums] * 3

print(nums_list)

allcase1 = itertools.product(nums, nums, nums)

for i in allcase1:
    print(i, end='')
print()

allcase2 = itertools.product(*nums_list)  # 모든 케이스를 입력받음
for i in allcase2:
    print(i, end='')

    