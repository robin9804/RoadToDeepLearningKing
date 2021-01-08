#Problem 106
sports = ['soccer']
sports.append('baseball')
sports.append('hocky')
print(sports)
sports.insert(1, 'tennis')
print(sports)
sports.sort()
print(sports)
print(sports.pop())
sports.reverse()
print(sports)
#Problem 128
list1 = []
for i in range(10):
    num = int(input('insert numbers:'))
    list1.append(num)
set1 = set(list1)
print(max(set1))
#Problem 142
my_list = input('Enter six numbers:').split()
my_str = ''
for i in range(len(my_list)):
    my_str = my_str + my_list[i]
j = 0
i = 0
num_list = []

while (i <= len(my_str)//3):
    num_list.append(int(my_str[j:j+3]))
    i += 1
    j += 3
print(sum(num_list))
#problem 151
string = input('Enter english sentence : ')
if string[0] in 'aeiou':
    print('Good Sentence')
#Problem 154
a, b, c = map(int, input('Enter three integer : ').split())
result1 = (a) if a<b else (b)
result2 = result1 if result1 < c else c
print(result2)
#Problem 170
n1 = int(input('first num : '))
n2 = int(input('second num : '))

n3 = n1 if (n1<n2) else n2 # Minimum Value
n4 = n1 if (n1>n2) else n2 # Maximum Value
j = n3//5+1
k = n4//5
while (j <= k):
    print(j*5)
    j += 1
#177
num = int(input('Enter a integer: '))
n = 0
for i in range(1, num+1):
    n += i
print('1부터 {}까지 합은 {}'.format(num, n))
#180
num = int(input('Enter a integer : '))
j = 0
for i in range(2, num//2):
    if num%i == 0:
        print('{} is not prime number'.format(num))
        j += 1
        break
if (j == 0):
    print('{} is prime number'.format(num))
#181
num = input('Enter the number: ')
num1 = list(num)
n = 0
for i in range(len(num1)):
    n += int(num1[i])
print('{}의 각 자리수의 합은 {}'.format(num, n))
#182
try:
    num = int(input('Enter the number : '))
    print(True)
except:
    print(False)
#183
a, b = map(int, input('Enter the two integers').split())
n1 = a if (a<b) else b #Min value
n2 = a if (a>b) else b
j = 0
if n1%2==0 and n2%2==0:
    list1 = [i for i in range(n1, n2+1, 2)]#even
    list2 = [i for i in range(n1+1, n2, 2)]#odd
    j = 1
elif n1%2==0 and n2%2!=0:
    list1 = [i for i in range(n1, n2, 2)]#even
    list2 = [i for i in range(n1+1, n2+1, 2)]#odd
    j = 2
elif n1%2!=0 and n2%2==0:
    list1 = [i for i in range(n1+1, n2+1, 2)]#even
    list2 = [i for i in range(n1, n2, 2)]#odd
    j = 3
else:
    list1 = [i for i in range(n1+1, n2, 2)]#even
    list2 = [i for i in range(n1, n2+1, 2)]#odd
    j = 4
n = 0
for i in range(len(list1)):
    n -= list1[i]
for i in range(len(list2)):
    n += list2[i]
if j == 1:
    for i in range(len(list2)):
        print('- {} + {} '.format(list1[i], list2[i]), end = '')
    print('- {} = {}'.format(list1[-1], n))
elif j == 2:
    for i in range(len(list2)):
        print(' - {} + {}'.format(list1[i], list2[i]), end='')
    print(' = {}'.format(n))
elif j == 3:
    for i in range(len(list2)):
        print('{} - {} + '.format(list2[i], list1[i]), end='')
    print(' = {}'.format(n))
else:
    for i in range(len(list1)):
        print('{} - {} + '.format(list2[i], list1[i]), end='')
    print('{} = {}'.format(list2[i], n))
#185
n = int(input('Enter your integer : '))
l = 1
while (n != 1):
    if (n%2 ==0 ):
        n /= 2
    else:
        n *= 2
        n += 2
    l += 1
print(l)
#187
for i in range(1, 10):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i, j, i*j))
#194
num = int(input('Enter the positive number: '))
biggest_prime = 1

list1 = []
for i in range(1, num):
    chk = True
    for j in range(2, i):
        if i % j ==0:
            chk = False
            break
    if chk:
        list1.append(i)
biggest_prime = max(list1)

print('biggest prime number under', num, 'is', biggest_prime)
#195
for x in range(0, 11):
    for y in range(0, 11):
        if (3*x+2*y==10):
            print('Solution is {} and {}.'.format(x, y))
##200
my_list = ['1', '2', '3', '4', '5']
list1 = []
for i in range(len(my_list)):
    for j in range(len(my_list)):
        if (j != i):
            for k in range(len(my_list)):
                if (k != i and k != j):
                    for x in range(len(my_list)):
                        if(x != i and x != j):
                            if (x != k):
                                for y in range(len(my_list)):
                                    if (y != x and y != i):
                                        if (y != j and y != k):
                                            list1.append(my_list[i]+my_list[j]+my_list[k]+my_list[x]+my_list[y])
for i in range(len(list1)):
    list1[i] = int(list1[i])
list1 = sorted(list1)
print(list1[49])
