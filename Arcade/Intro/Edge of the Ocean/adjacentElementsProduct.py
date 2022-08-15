def solution(inputArray):
    key = -1000000
    for i in range(0, len(inputArray)-1):
        if(key < inputArray[i]*inputArray[i+1]):
            key = inputArray[i]*inputArray[i+1]
           
            
                
    return key