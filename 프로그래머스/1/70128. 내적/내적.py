def solution(a, b):
    answer = 0
    
    for x,y in zip(a,b):
        nums=x*y
        answer+=nums
    
    return answer