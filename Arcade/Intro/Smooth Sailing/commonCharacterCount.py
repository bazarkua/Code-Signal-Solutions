def solution(s1, s2):
    
    d1 = {}
    d2 = {}
    res = 0
    
    for i in s1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    
    for i in s2:
        if i not in d2:
            d2[i] = 1
        else:
            d2[i] += 1
   
    for i in d1:
        if i in d2:
            res+=min(d1[i],d2[i])
        
    return res