
print('a = ', end = ' ')
a = int(input())
print('b = ', end = ' ')
b = int(input())
print('c = ', end = ' ')
c = int(input())
print('k = ', end = ' ')
d = int(input())

def Fermat(x, y, z, k):

    if k == 2:
        return 'Good'

    else:
        if (x**k + y**k) == (z**k):
            return 'Fermat is wrong'
        else:
            return Fermat(x,y,z,k-1)

print(Fermat(a,b,c,d))