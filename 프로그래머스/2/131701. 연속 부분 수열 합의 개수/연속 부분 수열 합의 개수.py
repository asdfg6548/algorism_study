def solution(elements):
    n = len(elements)
    # 원형 수열을 만들기 위해 리스트를 두 배로 늘림
    elements = elements * 2
    # 중복을 제거하기 위한 set
    result = set()
    
    # 부분 수열의 길이
    for length in range(1, n + 1):
        # 시작 위치
        for start in range(n):
            # 연속 부분 수열의 합 계산
            sum_value = sum(elements[start:start + length])
            result.add(sum_value)
    
    return len(result)