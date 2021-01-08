
nums = list(range(1,10))

i = 1
j = 1

for i in nums:
    
    for j in nums:
    
        print('{} X {} = {}'.format(i,j,i*j))
        
        j += 1
        
    i += 1
    
    
