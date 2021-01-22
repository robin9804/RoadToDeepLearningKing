

def num_rabbit(month):

    if month == 1:

        return 2

    elif month == 2:

        return 2

    else:

        return num_rabbit(month-1) + num_rabbit(month-2)


print(num_rabbit(11))   # 답 : 178?
