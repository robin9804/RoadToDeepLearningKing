# problem 182

num = input('Enter the number : ')

result = True

try:
    num = float(num)
except:
    result = False

print(f'{num} is number? : {result}')
