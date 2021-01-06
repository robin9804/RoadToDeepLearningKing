# problem 194
num = int(input('Enter the positive number : '))
biggest_prime = 1

for i in range(1, num):
    mod = 0
    for j in range(2, i):
        if i % j == 0:
            mod += 1
            print(i, ' = i, j=', j)
            break
        else:
            pass
    if mod == 0:
        biggest_prime = i

print('biggest prime num = ', biggest_prime)