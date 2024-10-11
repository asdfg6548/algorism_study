def solution(nums):
    answer = 0
    
    pick=len(nums)//2
    kind=len(set(nums))
    
    # 종류보다 선택 할 포켓몬 수가 적은 경우
    if pick < kind:
        answer=pick
    # 나머지 경우(종류보다 선택할 포켓몬 수가 더 크거나 같음)
    else:
        answer=kind
    
    return answer
