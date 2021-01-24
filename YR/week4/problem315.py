# problem 315

import itertools

num = [i for i in range(1, 7)]

print(num)

nums = [num] * 6

result = itertools.permutations(num)
ans = 0
for i in result:
    print(i, end='')
    ans += 1

print()
print(ans)
