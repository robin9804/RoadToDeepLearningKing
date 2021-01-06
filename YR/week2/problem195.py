# problem 195, Solve
print('solve 3x + 2y = 10')

for x in range(11):
    for y in range(11):
        sol = True if (3*x + 2*y == 10) else False
        if sol:
            print('the solution is x =',x, ', y=',y)
            break
