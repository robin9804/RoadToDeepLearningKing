# problem 342

import math
import sys

print('이차방정식')

a = float(input('A : '))
b = float(input("B : "))
c = float(input('C : '))

if a == 0:
    print('not a quadratic function')
    sys.exit()

D = b * b - 4 * a * c
if D>0:
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    print('solution 2 : ', x1, x2)

elif D == 0:
    x = -b / (2*a)
    print('one solution', x)

else:
    print('no solution')

    