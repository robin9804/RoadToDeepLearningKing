

print('Enter the number :', end = ' ')
n = int(input())

def HandsomeQ(x):

    nums = [n]

    while x != 1:
    
        if x % 2 == 0:
            x = x / 2
            
        else:
            x = 2 * x + 2
            
        nums = nums + [x]
    
    return nums
    
print(len(HandsomeQ(n)))