

print('Enter the number :')
num = input()

try:
    s = float(num)
    print('{} is numbers? True'.format(num))
except:
    print('{} is numbers? False'.format(num))
    