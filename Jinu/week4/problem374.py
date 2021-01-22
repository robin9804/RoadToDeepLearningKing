

money = [0 for i in range(1,13)]
money[0] = 1000000

sum = 1000000
count = 0

for i in range(1,12):

    print(i+1, "월 달 입금 금액 : ")
    money_in = int(input())
    sum += money_in

    if (money[i-1] != 0) & (money[i] != 0):

        count += 1

        sum = sum * (0.01*(1 + (0.05*count)))

    else:

        count = 0
        sum = sum * 1.01

print(int(sum))