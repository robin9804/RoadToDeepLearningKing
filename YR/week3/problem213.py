# probelm 213

num = input('new number')

while len(num) != 1:
    new_num = 0
    for i in num:
        new_num += int(i)
    new_num = str(new_num)
    num = new_num

print(num)
