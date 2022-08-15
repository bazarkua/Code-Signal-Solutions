def solution(inputArray):
    
    maxLen = 0
    maxArray = []

    for i in inputArray:
        maxLen = max(len(i), maxLen)
    
    for i in inputArray:
        if len(i) == maxLen:
            maxArray.append(i)
    
    return maxArray
    