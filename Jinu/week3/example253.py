
def fun(n) :
    if n == 0:
        return 1

    elif n % 2 == 1:
        return fun(n-1) * 2 - 1

    else : 
        return fun(n-2) +3

for i in range(10) :
    print(fun(i), end = ' ')