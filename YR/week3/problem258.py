# problem 258

def exp_an(a, n):
    if n == 0:
        return 1
    else:
        return exp_an(a, n-1) * a

print(exp_an(3, 4))