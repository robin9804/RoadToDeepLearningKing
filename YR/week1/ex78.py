# ex 78

string = 'Hello, my Name is YoungROk Kim'

print(string.upper())  # 대문자로 바꿔주는 함수
print(string.lower())  # 모두 소문자로 바꿔주는 함수
print(string.title())  # 앞글자만 대문자로 만들어주는 함수
print('\n')

print(string.count('i'))
print(string.endswith('m'))  # 끝자리가 뭐로 끝나는지 확인하는 함수
print(string.startswith('h')) # 앞에가 뭐로 끝나는지 확인하는 함수
print(string.lower.startswith('h'))  # 이렇게 복합적으로도 사용가능

str1 = string.split()  # 띄어쓰기 기준으로 리스트로 만들기
str2 = string.split(',')  # 쉼표 기준으로 리스트 만들기
print(str1)
print(str2)
