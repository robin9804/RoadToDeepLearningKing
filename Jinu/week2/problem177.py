
print("정수를 하나 입력하시오 : ")
n = int(input())

nums = list(range(n+1))

i = 0
sum = 0

for i in nums:
    sum = sum + i
    i += 1
    
print(sum)