
numbers = input().split()

num = "".join(numbers)

print(num)

def n(a,b):
    nn = num[a:b]
    return nn

print('{} + {} + {} + {} = {}'.format(n(0,3), n(3,6), n(6,9), n(9,11),
    int(n(0,3))+int(n(3,6))+int(n(6,9))+ int(n(9,11))))     #빡세다 이문제 ,,,