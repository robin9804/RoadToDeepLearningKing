
print('밑 : ' , end= '')
x = int(input())
print('지수 : ', end = '')
y = int(input())

def exp(a, n):

    if n == 0:
        return 1

    else: 
        return a * exp(a,n-1)

print(x, '^' , y, '=', exp(x,y))