# problem 325

import itertools
import math


print(math.sqrt(108) - 1)

answer = 0
for y in range(1, 11):
    for x in range(1, y + 1):
        print(x, y)
        if math.sqrt(x * y) + x + y == 108.0:
            answer += 1

print(answer)