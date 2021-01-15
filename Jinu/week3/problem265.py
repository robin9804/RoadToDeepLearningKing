

def f(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2

    elif n % 2 == 1:
        return 2 * f(n-1) - 1
    elif (n % 2 == 0) & (n % 10 != 0):
        return f(n-1) + 2
    elif n % 10 == 0:
        return (5 * f(n-1)) - (7 * f(n-5))

print(f(10))