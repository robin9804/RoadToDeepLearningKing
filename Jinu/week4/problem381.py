
nums = list(map(int,input().split()))

binums = [1 for m in range(len(nums))]
ans = [1 for n in range(len(nums))]


def binary(a):

	for i in range(1111):
		try:
			if a == int(str(i),2):
				return str(i).zfill(2)
				break

		except:

			i += 1

def revised(x):

	if x == 0:
		return '0'

	elif x == 1:
		return '101'

	elif x == 2:
		return '110'

	elif x == 3:
		return '111'

for j in range(len(nums)):

	binums[j] = binary(nums[j])
	ans[j] = revised(nums[j])

print(binums)
print(ans)

