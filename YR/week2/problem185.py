# problem 185
n = input('Enter the number : ')
n = int(n)

order = 1

while n!=1 :
    if n % 2 == 0:
        n /= 2
        print(n)
    else:
        n = 2*n + 2
        print(n)
    order += 1

print(order)