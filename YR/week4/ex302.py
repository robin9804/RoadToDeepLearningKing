
def summ(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


sum = 0
for i in range(100):
    sum += summ(i)
print(sum)