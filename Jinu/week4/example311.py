
mylist = []

list = [1,2,3,4,5,6]

for i in list:
    for j in list:
        for k in list:
            for l in list:
                for m in list:
                    for n in list:
                        if len({i,j,k,l,m,n}) == 6:     # 중복 없이 한번씩 번호 출력
                            mylist += [[i,j,k,l,m,n]]

print(len(mylist))


def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]

        for p in permutation(remLst):
            l.append([m] + p)               # 리스트 내의 숫자 하나를 빼낸 후, 맨 앞으로 보냄. 이를 반복하여 숫자 조합
        
    return l

a = permutation([1,2,3,4,5,6])
print(len(a))


import itertools

mylist = [1,2,3]

myp = itertools.permutations(mylist)        # 순열
for i in myp:
    print(i, end = ' ')
print()

myc = itertools.combinations_with_replacement(mylist,3)     # 중복 조합
for i in myc:
    print(i, end = ' ')
print()

myc2 = itertools.combinations(mylist,3)
for i in myc2:
    print(i, end = ' ')
