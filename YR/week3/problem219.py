# problem 219

def fun_recurring(N):
    num = 1/N
    num = str(num)
    if len(num) < 10:
        return 0
    else:
        # 순환마디 구하기
        num = num[2:]
        result = num
        for n in range(len(num)//2):
            print(num[0:n], ' vs ', num[n : n+n])
            if num[0:n] == num[n:n+n]:
                result = num[:n]
                
        return result



a = 7
print(a)
print(fun_recurring(a))