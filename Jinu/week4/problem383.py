
n = int(input('n을 입력하세요 : '))

nums = [[] for i in range(n)]

for j in range(n):

    nums[j] = list(map(int,input().split()))


def get_trace(list1):

    trace = 0

    for m in range(len(list1)):

        trace += list1[m][m]

    return trace

def det(x):

    ans = (x[0][0] * (x[1][1]*x[2][2] - x[2][1]*x[1][2])) + (x[0][1] * ( x[1][2]*x[2][0]) - x[1][0]*x[2][2]) + (x[0][2] * (x[1][0]*x[2][1] - x[1][1]*x[2][0]))
    return ans


def get_determinant(list2):

    if len(list2) == 2:

        return deter

    elif len(list2) == 3:

        deter = det(list2)
        return deter

print(get_trace(nums), det(nums))

''' 3차 행렬의 determinant만 구함.... 4차 이상에서는 재귀함수로 구해보려했지만 실패... '''