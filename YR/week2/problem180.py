# problem 180, 소수판별
num = input('Enter the number : ')
num = int(num)

prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
        print(f'{num} is not prime number')
        break
    else:
        pass

if prime:
    print(f'{num} is prime number')