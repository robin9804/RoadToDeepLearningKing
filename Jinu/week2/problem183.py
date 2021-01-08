
print("Enter the 1st nubmer : ")
n1 = int(input())
print("Enter the 2nd number : ")
n2 = int(input())

if n1 > n2:
    nums = list(range(n2,n1+1))
    large = n1
    small = n2
else:
    nums = list(range(n1,n2+1))
    large = n2
    small = n1
    
i = small
sum = 0

chars = list(range(small,large+1))

while i <= large:
    j = i - small
    if nums[j] % 2 == 0:
        char = '- {}'.format(nums[j])
        chars[j] = char
        nums[j] = nums[j] * (-1)

    else:
        nums[j] = nums[j]
        char = '+ {}'.format(nums[j])
        chars[j] = char

    sum = sum + nums[j]
    print(chars[j], end=' ')
    
    i += 1
    
print('=', end = ' ')
print(sum)
