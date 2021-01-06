# problem 177

num = input('정수를 하나 입력하시오 : ')

num = int(num)

result = 0
for i in range(num + 1):
    result += i

print(f'1 부터 {num} 까지의 합은 {result}')