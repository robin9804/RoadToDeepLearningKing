# problem 210

def fun(n):
    answer = 0
    for i in range(n):
        answer += i % 5
    print('fun({})의 return 값은 {}이다'.format(n, answer))
    return answer

a = int(input('number :: '))
fun(a)