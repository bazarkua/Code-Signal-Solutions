def solution(year):
    century = 0
    if(year>=1 and year <= 100):
        return 1
    else:
        if(year%100>0):
            return ((year//100)+1)
        else:
            return year//100
            