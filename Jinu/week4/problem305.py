
count = 0

for i in range(1,4):

    for j in range(i+1, 5):

        for k in range(j+1, 6):

            print(i, j, k)
            count += 1

print(count)