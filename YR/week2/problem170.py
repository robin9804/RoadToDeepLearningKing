# problem 170
first = input('first num : ')
second = input('Second num : ')

first = int(first)
second = int(second)

little = (first) if first < second else (second)
big = (first) if first > second else (second)


if first == second:
    print('Error, Two numbers are same')

else:
    five_first = little // 5 + 1  # 5로 나눈 몫 + 1
    while five_first * 5 < big:
        print(five_first * 5)
        five_first += 1
