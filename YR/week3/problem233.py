r1 = list((input('첫 번째 행을 입력해주세요 ').split()))
r2 = list(input('두 번째 행을 입력해주세요 ').split())
r3 = list(input('세 번째 행을 입력해주세요 ').split())

r1 = [int(i) for i in r1]
r2 = [int(i) for i in r2]
r3 = [int(i) for i in r3]

from math import floor

print('가로 평균 :{} {} {}'.format(((r1[0])+(r1[1]))/2, (r2[0]+r2[1])/2, (r3[0]+r3[1])/2))
print('세로 평균 :{} {}'.format((r1[0]+r2[0]+r3[0])/3, (r1[1]+r2[1]+r3[1])/3))
print('전체 평균 :{}'.format((sum(r1) + sum(r2) + sum(r3))/ 6))
