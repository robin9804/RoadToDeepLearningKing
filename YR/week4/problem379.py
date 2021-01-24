# problem 379

def increase(listin):
    answer = []
    for i in range(len(listin)-1):
        if listin[i] > listin[i+1]:
            answer.append(i+1)
    answer.append(len(listin))

    if len(answer) == 1:
        return listin
    else:
        k = 0
        ref = 0
        for j in range(len(answer)-1):
            if answer[j+1] - answer[j] > k:
                k = answer[j+1] - answer[j]
                ref = answer[j]
        return listin[ref:ref + k]


arr = [1,2,3,7,4,5,6]
print(arr[0:len(arr)])
print(increase(arr))