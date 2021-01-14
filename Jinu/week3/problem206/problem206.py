
score = int(input("점수를 입력하시오 :"))

if (score <= 100) & (score >= 90):
    grade = 'A'
    print(grade)

elif (score < 90) & (score >= 80):
    grade = 'B'
    print(grade)

elif (score < 80) & (score >= 70):
    grade = 'C'
    print(grade)

elif (score < 70) & (score >= 60):
    grade = 'D'
    print(grade)

else:
    grade = 'F'
    print(grade)


