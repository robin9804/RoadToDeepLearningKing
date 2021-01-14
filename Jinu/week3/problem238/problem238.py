
print('숙제를 제출한 출석번호 : ', end = ' ')
nums = input().split()

i = 0

students = list(range(20))
i = 0

for i in range(20):

    students[i] += 1

j = 0

while j < len(nums):

	if int(nums[j]) in students:

		students.remove(int(nums[j]))

	j +=1

print(students)

