# Ex 251, 재귀함수의 정의
def printHello(n):
    print('hello')
    printHello(n-1) if n>1 else None

printHello(5)
