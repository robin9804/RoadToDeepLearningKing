
print('Enter the number : ')

a = int(input())

nums = list(range(a))



def prime_test(x):

    i = 1
    count = 0
    
    while i < x:
        rest = x % i
        if rest == 0:
            count += 1
        i += 1
    
    if count == 1:
        print('{} is prime number'.format(x))
    else:
        print('{} is not prime number'.format(x))
        
prime_test(a)