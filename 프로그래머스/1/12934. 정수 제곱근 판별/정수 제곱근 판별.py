def solution(n):
   # n의 제곱근을 계산
    sqrt_n = n ** 0.5
    
    # 제곱근이 정수인지 확인
    if sqrt_n.is_integer():
        # 정수라면 (sqrt_n + 1)^2 반환
        return int((sqrt_n + 1) ** 2)
    
    else:
        # 아니라면 -1 반환
        return -1