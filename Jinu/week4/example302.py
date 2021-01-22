

def sum(n):

    sum = 0

    for i in range(n+1):

        sum += i

    return sum

answer = 0

for i in range(100):
    answer += sum(i)

print(answer)