
''' 도저히 못하겠어서... 유한인지 무한인지 판별만 했슴다'''

n = int(input('정수 입력 : '))

def fun_recurring(x):

    num = str(1 / x)
    nums = num.strip('0.')

    if ('e' in nums) == False:
        res = 0

    elif ('e' in nums) == True:
        res = 1

    return res


print(fun_recurring(n))