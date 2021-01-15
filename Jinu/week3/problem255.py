
print('숫자 입력 = ' , end = ' ')
n = int(input())

def factorial(x):

    if x == 1:
        return 1

    else:
        return x * factorial(x-1)


print(n , '! = ' , factorial(n))