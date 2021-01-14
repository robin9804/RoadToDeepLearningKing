
n = int(input('자연수 n 입력 : '))

def fun(x):

    i = 0
    sum = 0

    for i in range(x):

        mod = i % 5
        sum = sum + mod

    return sum

print(fun(n))