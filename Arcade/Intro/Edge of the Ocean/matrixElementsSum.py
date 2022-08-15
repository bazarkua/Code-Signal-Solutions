def solution(matrix):
    
    maxSum = 0
    
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if(i == 0):
                maxSum += matrix[i][j]
                continue
            else:
                if((matrix[i-1][j] != 0) and matrix[0][j] != 0):
                    maxSum += matrix[i][j]
                else:
                    continue
                
            print(maxSum)
    return maxSum
    