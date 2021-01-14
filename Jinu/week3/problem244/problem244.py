
print('Enter the numbers', end = ' ')

nums = input().split()

i = 0

while i < len(nums):
	print(nums)
	nums.append(nums[0])
	del nums[0]
	i += 1
