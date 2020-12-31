string = "Hello. My name is Haemin Park"

print(string.upper())   # 문자열을 대문자화
print(string.lower())   # 문자열을 소문자화
print(string.title())   # 각 단어의 첫 문자를 대문자화
print(len(string))      # 문자열의 길이 측정
print()

print(string.count('i'))        # ''라는 문자 개수 세기
print(string.endswith('k'))     # 마지막 문자가 ''인지 여부
print(string.startswith('h'))   # 첫 문자가 ''인지 여부
print(string.lower.startswith('h'))
print()

string_1 = string.split()       # 문자열을 공백을 기준으로 자른 후, 리스트에 저장
string_2 = string.split(',')    # 문자열을 ''안의 문자를 기준으로 자른 후, 리스트에 저장
print(string_1)
print(string_2)