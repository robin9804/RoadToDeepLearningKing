ints = int(input('Enter the number : '))


for i in range(ints):
    result = []
    for j in range(1, ints+1):
        result.append(str(j + ints * i))
        if i % 2 == 1:
            result.reverse()
    print(' '.join(result))
