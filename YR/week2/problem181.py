# problem 181 각 자리수를 더하는 프로그램
num = input('Enter the number : ')

result = 0
for i in num:
    result += int(i)

print(f'{num} 의 각 자리수의 합은 {result}')
