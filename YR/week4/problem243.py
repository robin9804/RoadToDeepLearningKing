# problem 342

import math
import sys

print(" ax2 + bx + c = 0")

a = float(input("a ? "))
b = float(input("b ? "))
c = float(input("c ? "))

if a == 0:
    print("a == 0, 이차방정식이 아닙니다.")
    sys.exit()
    
D = b * b - 4 * a *c
if D>0:
    solution1 = -1 * b - math.sqrt(D) / (2 * a)
    solution2 = -1 * b + math.sqrt(D) / (2 * a)
    print(solution1, ', ', solution2)

elif D ==0:
    x = -b / a
    print('1개의 해: ', x)

else:
    print("해가 없습니다.")