# problem 247
num_in = input('Enter the number : ').split()

arr = []
for i in range(int(num_in[0])):
    arrs = []
    for j in range(int(num_in[1])):
        arrs.append(i + j)
    arr.extend(arrs)

new_arr = sorted(arr)
print(sorted(arr))

result = [str(i+1) for i in range(int(num_in[0]) * int(num_in[1]))]
results = dict(zip(result, new_arr))

print(results)

print(results[2])

