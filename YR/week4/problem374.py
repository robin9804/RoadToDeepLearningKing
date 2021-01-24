# problem 374

# 매달 1%의 복리, n달에는 1+0.05%의 이자

final_month = 12
def bank(money, date):
    if date == 1:
        return money
    else:
        print(money, ',', date)
        return bank(money * (1+0.01 + 0.0005*(final_month-date)), date-1)

bank(1000000, 12)