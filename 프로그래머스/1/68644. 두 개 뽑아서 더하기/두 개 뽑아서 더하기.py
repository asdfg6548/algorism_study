from itertools import combinations
def solution(numbers):
    res=[]
    lis=list(combinations(numbers,2))
    
    for n in lis:
        res.append(sum(n))
    
    answer=list(set(res))
    answer.sort()
        
    return answer