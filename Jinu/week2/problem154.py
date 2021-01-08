
a = input()
b = input()
c = input()

if a >= b:
    res = a if a > c else c
else:
    if b >= c:
        res = b
    else:
        res = c
        
print(res)