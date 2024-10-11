def solution(nums):
    answer = 0
    
    pick=len(nums)//2
    kind=len(set(nums))
    
    if pick < kind:
        answer=pick
    else:
        answer=kind
    
    return answer
