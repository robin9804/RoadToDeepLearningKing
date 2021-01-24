# example 312

import itertools

nums = [1, 2, 3]

# 중복순열을 통한 3개 나열하는 경우의 수
allcase = itertools.product(nums, nums)

for i in allcase:
    print(i, end='')
