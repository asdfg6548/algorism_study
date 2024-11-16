def solution(arr):
    """N개의 수의 최소공배수를 구하는 함수"""
    max_num = max(arr)  # 주어진 수들 중 최대값
    answer = max_num    # 최소공배수는 최소한 최대값 이상
    
    while True:
        is_lcm = True   # 현재 수가 최소공배수인지 확인하는 플래그
        
        # 현재 숫자(answer)가 모든 입력값들을 나누어 떨어뜨리는지 확인
        for num in arr:
            if answer % num != 0:  # 하나라도 나누어 떨어지지 않으면
                is_lcm = False     # 최소공배수가 아님
                break
        
        if is_lcm:          # 모든 수를 나누어 떨어뜨리면
            return answer   # 현재 값이 최소공배수
            
        answer += max_num   # 최대값만큼 증가 (최적화)