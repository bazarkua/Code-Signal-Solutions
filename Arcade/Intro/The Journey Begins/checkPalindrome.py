def solution(inputString):
    key = ""
    for i in range(len(inputString)-1,-1,-1):
        key = key+inputString[i]
    if(key == inputString):
        return True
    else:
        return False
        