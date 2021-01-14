
n = input('수 입력 : ')

i = len(n)

while i > 1:

    j = 0
    sums = 0 

    for j in range(len(n)):

        n_int = int(n[j])
        sums = sums + n_int
    i = len(str(sums))
    n = str(sums)

print(sums)
