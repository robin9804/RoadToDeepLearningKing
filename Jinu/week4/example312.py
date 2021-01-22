
import itertools

nums = [1,2,3,4,5]

allcase = itertools.product(nums, nums, nums)     # list 중 3개 조합
for i in allcase:
    print(i, end=' ')