# problem 142
nums = input('insert 6 numbers: ') # 6개의 정수 입력
nums.split()

# 모두 붙여서 문자열로 저장
number = ''
for i in nums:
    if i != ' ':
        number += i
print(number)

# 세 자씩 나누어 수 들의 합을 출력하기
number = list(number)
length = len(number) //3
print(length // 3)  # 3으로 나눴을 때 몫이 얼마나 나오는지 확인하기
sum = 0
for i in range(length):
    num1 = ''
    for j in range(3):
        num1 += number[i*3+j]
    sum += int(num1)

if len(number) % 3 == 0:
    print(sum)

else:
    num2 = ''
    for k in number[length * 3 :]:
        num2 += k
    sum += int(num2)
    print(sum)