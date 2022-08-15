def solution(a):
    
    aSorted = sorted(a)
        
    
    countTrees = a.count(-1)    

    i = 0
    j = countTrees
    
    while i < len(a):
        
        if(a[i] != -1):
            a[i] = aSorted[j]
            i += 1
            j += 1  
        
        else:
            i+=1     
    
    return a