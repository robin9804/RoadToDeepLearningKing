
my_list = [1,2,3,4,5,6]

str = "Hello World"

my_list[0]
str[0]

3 in my_list
"H" in str

my_list.index(5)
str.index("r")


characters  = list('abcdef')

words = "Hello world는 프로그래밍을 배우기에 아주 좋은 사이트 입니다."

words_list = words.split()  # 각 단어들이 띄워쓰기 기준으로 나뉨   **** 문자열이 나뉜 후에 list로 저장*****

time_str = "10:35:27"
time_list = time_str.split(":") # 각 단어들이 :를 기준으로 나뉨

":".join(time_list)         # :를 기준으로 다시 결합됨
" ".join(words_list)        # 띄어쓰기를 기준으로 다시 결합됨