# problem 183
A = input('enter 1st number :')
B = input('enter 2nd number :')

a = int(A)
b = int(B)

answer = 0
sik = ''
for i in range(a, b+1):
    if i % 2 == 1:
        answer += i
        sik += '+' + str(i)
    else:
        answer -= i
        sik += '-' + str(i)

print(sik)
print('=',answer)