# prob 93
num = input("네 수를 입력하세요")
num = num.split()
num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])
num4 = int(num[3])
average = (num1+num2+num3+num4)/4
print('평균 : %.1f'%average)
variance = ((num1-average)**2 + (num2-average)**2 + (num3-average)**2 + (num4-average)**2) / 4
print('분산 : %.1f'%variance)