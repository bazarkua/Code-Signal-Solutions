n = 1230
n = 239017

def solution(n):
    stringn = str(n)
    firstHalf = 0
    secondHalf = 0
    HalfLength = len(stringn)//2

    for i in range(0, HalfLength):
        firstHalf += int(stringn[i])
    
    for i in range(HalfLength, len(stringn)):
        secondHalf += int(stringn[i])
    
    if(firstHalf == secondHalf):
        return True
    else:
        return False


print(solution(n))
