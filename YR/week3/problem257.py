# problem 257 - 피보나치 수열

def pibonazzi(n):
    if n == 1 or n == 2: 
        return 1
    else:
        return pibonazzi(n-1) + pibonazzi(n-2)

print(pibonazzi(6))