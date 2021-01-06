# problem 200
# 1부터 5까지 숫자를 단 한번씩만 써서 만든 다섯 수들을
# 가장 작은 수부터 커지는 순서로 나열했을 때 50번째로 오는 수를
# 구해라
# 54321, 54312, ... b
base = [1,2,3,4,5]
result_list = []

# 5 * 4 * 3 * 2 * 1
result = 0
for num1 in range(1, 6):
    base.remove(num1)
    base2 = base.copy()
    for num2 in base2:
        base.remove(num2)
        base3 = base.copy()
        for num3 in base3:
            base.remove(num3)
            base4 = base.copy()
            for num4 in base4:
                base.remove(num4)
                base5 = base.copy()
                for num5 in base5:
                    result = num1*10000+num2*1000+num3*100+num4*10+num5

                    result_list.append(result)
    base = [1, 2, 3, 4, 5]

print(result_list)
print(len(result_list))
print(5*4*3*2)
#print('answer is 50th ', result_list[49])
# 재귀 형태의 함수가 되어야 하지 않나...?
