num = input('숙제를 제출한 출석번호 : ').split()

print(num)
total_student = [str(i) for i in range(1, 21)]

for i in num:
    total_student.remove(i)

for i in total_student:
    print(i, end=' ')
