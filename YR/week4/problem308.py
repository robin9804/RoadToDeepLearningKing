# problem 308

def breth(n):
    if n == 2 or n == 1:
        return 2
    else:
        return breth(n-1) + breth(n-2)

print(breth(11))