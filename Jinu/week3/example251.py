
def printHello(n) : 
    print('Hello!')
    printHello(n-1) if n > 1 else None

printHello(5)