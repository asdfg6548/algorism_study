def solution(a, b):
    answer = 0
    
    n=max(a,b)
    
    if a < b :
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))
