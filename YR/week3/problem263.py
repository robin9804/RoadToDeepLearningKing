# problem 263

N, M = list(input("enter the ints : ").split())
N, M = int(N), int(M)

def sum_list(l1, l2):
    lists = []
    for i in l1:
        for j in l2:
            lists.append(i + j)
    return lists

def func(N ,M):
    lists = []
    if N == 1:
        if M in range(1, 7):
            return [[M]]
        else:
            return False
    else:
        for i in range(1, 7):
            if func(N-1, M-i) != False:
                lists += sum_list([[i]], func(N-1, M-i))
    return lists

print(func(N, M))
print(len(func(N, M)))