# ex 253 재귀적 호출이 가능한 함수

def fun(n):
    # 중단점 설정
    if n == 0:
        return 1
    # 조건에 따른 반복적인 행위
    elif n%2 == 1:
        return fun(n-1) * 2 - 1
    else:
        return fun(n-2) + 3

for i in range(10):
    print(fun(i))