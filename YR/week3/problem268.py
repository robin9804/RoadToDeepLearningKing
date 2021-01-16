# problem 268

def fermat(a, b, c, k):
    for i in range(3, k+1):
        if a ** i + b ** i == c **i :
            print('Fermat is wrong')
            break
    print('good')

fermat(3,4,5,7)