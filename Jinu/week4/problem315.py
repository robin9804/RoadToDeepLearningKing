
# case 1

list = [0,1,2,3,4,5]
count = 0

for i in range(len(list)-1):
    for j in list:
        for k in list:
            for l in list:
                for m in list:
                    for n in list:

                        if len({i,j,k,l,m,n}) == 6:
                            count += 1

print(count)

# case 2

import itertools

permu = itertools.permutations(list)
count2 = 0

for i in permu:
    count2 += 1

permu_0 = itertools.permutations(list[1:])
count3 = 0

for j in permu_0:
    count3 += 1

ans = count2 - count3
print(ans)