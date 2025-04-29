from itertools import combinations

def solution(number):
    answer = 0
    
    lis=list(combinations(number,3))
    
    for num in lis:
        if sum(num)==0:
            answer+=1
    
    return answer