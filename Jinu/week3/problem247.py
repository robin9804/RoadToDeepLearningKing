
''' 규칙을 못찾겠음.... '''


print('Enter the number : ' , end = ' ')
num = input().split()

i = 0
for i in range(2):
    num[i] = int(num[i])


j = 0
k = 0

arr = [[1 for j in range(num[1])] for k in range(num[0])]

for j in range(num[0]):
    for k in range(num[1]):

        arr[j][k] = arr[j][k-1] + k         # 첫번째 행은 만듦


    print(arr[j])