# problem 151

print('=== Determine Good Sentense ===')
sen = input('Input Sentense: ')

aeiou = ['a', 'e', 'i', 'o', 'u']

sen = sen.lower()

print(sen)
if sen[0] in aeiou:
    print('True')
else:
    print('False')

# 삼항 연산 예제

a = 10
b = 20
result = (a-b) if a==b else (a+b)