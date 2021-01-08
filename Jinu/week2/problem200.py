

num = list(range(1,6))

for a in num:
    
    for b in range(num[1],num[4]):
    
        for c in range(num[2],num[4]):
        
            for d in range(num[3],num[4]):
                
                d = num[3]
                e = num[4]
                num[3], num[4] = num[4], num[3]
                print(a,b,c,d,e)
                
            num[2], num[3] = num[3], num[2]

    num[0], num[1] = num[1], num[0]
    #num[0], num[1], num[2], num[3], num[4] = num[1], num[2], num[3], num[4], num[0]
    # num[1], num[2], num[3], num[4], num[0] = num[2], num[3], num[4], num[0], num[1]
    # num[2], num[3], num[4], num[0], num[1] = num[4], num[0], num[1], num[2], num[3],
    # num[3], num[4], num[0], num[1], num[2] = num[0], num[1], num[2], num[3], num[4] 
    
