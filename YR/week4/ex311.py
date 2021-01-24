# example 311

# permutation 정의

mylist = []
list = [i for i in range(1, 7)]

for i in list:
    for j in list:
        for k in list:
            for l in list:
                for m in list:
                    for n in list:
                        if len({i, j, k, l , m, n}) == 6:
                            mylist.append([i, j, k, l, m, n])

print(len(mylist))

def permulation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    l = []
    for i in range(len(lst)):
        m = lst[i]
        remlst = lst[:i] + lst[i + 1:]

        for p in permulation(remlst):
            l.append([m] + p)

    return l

a = permulation(list)

print(len(a))

# itertools의 permutations, combinations, combination_with_replacement 함수를 사용하면 된다.

import itertools

print(itertools.permutations(list))

print(itertools.combinations(list, 3))

print(itertools.combinations_with_replacement(list, 3))

# 주소를 리턴할줄이야