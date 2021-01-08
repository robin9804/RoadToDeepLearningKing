
print("first num : ")
fn = int(input())
print("second num : ")
ln = int(input())

small = fn if fn<ln else ln
large = fn if fn>ln else ln

i = small

while i < large:

    if i % 5 == 0:
        print(i)

    i += 1
