
print("숫자 입력 : " , end = ' ')
n = int(input())

def fibonacci(x):

    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


print(fibonacci(n))