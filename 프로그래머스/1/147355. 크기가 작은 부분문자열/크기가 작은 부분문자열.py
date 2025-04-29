def solution(t, p):
    p_num = int(p)
    p_len = len(p)
    count = 0
    
    # 길이 len(p)인 부분문자열 추출
    for i in range(len(t) - p_len + 1):
        substring = t[i:i + p_len]
        # 부분문자열을 숫자로 변환해 비교
        if int(substring) <= p_num:
            count += 1
    
    return count