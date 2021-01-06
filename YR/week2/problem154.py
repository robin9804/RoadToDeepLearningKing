# problem154
a = input('Input A... ')
b = input('Input B... ')
c = input('Input C... ')

aorb = a if a<b else b
result = aorb if aorb < c else c
print('the minimun value is ', result)