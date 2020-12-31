

print('네 수를 입력하세요 :', end= ' ')
a = int(input())
b = int(input())
c = int(input())
d = int(input())     # 어떻게 한 줄에 입력을 다 받지??


aver = float((a + b + c + d) / 4)

def aa(x):
    res = (x - aver) ** 2
    
    return res

boonsan = float((aa(a) + aa(b) + aa(c) + aa(d)) / 4)

print("평균 : {}".format(aver))
print("분산 : {}".format(boonsan))