def solution(N, stages):
    answer = []
    
    # 각 스테이지 별 도달한 플레이어수와 클리어하지 못한 플레이어 수 계산
    for stage in range(1,N+1):
        reached=0
        not_cleared=0
        
        #stage 배열 순회
        for user_stage in stages:
            if user_stage>=stage:
                reached+=1
            if user_stage==stage:
                not_cleared+=1
        
        #실패율 계산
        if reached==0:
            fail_rate=0
        else:
            fail_rate=not_cleared/reached
            
        answer.append((stage,fail_rate))
    
    answer.sort(key=lambda x:(-x[1],x[0]))
    
    return [stage for stage, _ in answer]