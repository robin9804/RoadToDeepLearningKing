    
    
num = int(input('Enter the positive number : '))
biggest_prime = 1
    
for i in range(1,num):
    
    count = 0

    
    for j in range(1,i+1):

        
        if i % j == 0:

            count = count + 1
                                  
        j += 1
    
    if count == 2:
        
        biggest_prime = i      
        
    i += 1
    
print('biggest prime number under', num, 'is', biggest_prime)

