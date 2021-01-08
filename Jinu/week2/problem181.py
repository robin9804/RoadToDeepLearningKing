
print('Enter the number :')
num = input()

nums = list(num)

def sum(a):
    i = 0
    s = 0
    while i < len(nums):
        s = s + int(nums[i])
        i += 1
    return s

print('{} 의 각 자리수의 합은 {}'.format(num, sum(num)))