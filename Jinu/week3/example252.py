

def sum1(n):
    result = 0
    for i in range(1,n+1):
        result += i

    return result

def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n-1)

print(sum1(50), sum2(50))

