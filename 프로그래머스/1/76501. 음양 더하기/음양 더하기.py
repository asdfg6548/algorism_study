def solution(absolutes, signs):
    answer=0
    # zip 함수 사용
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
            
        else:
            answer-=absolute
            
    return answer