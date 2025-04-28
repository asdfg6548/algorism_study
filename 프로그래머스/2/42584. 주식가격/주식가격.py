def solution(prices):
    n = len(prices)
    answer = [0] * n  # 초기값 0
    stack = []  # 인덱스를 저장하는 스택
    
    for i in range(n):
        # 스택이 비어있지 않고, 현재 가격이 스택 top의 가격보다 작으면
        while stack and prices[stack[-1]] > prices[i]:
            prev = stack.pop()  # 가격이 떨어진 시점
            answer[prev] = i - prev  # 기간 계산
        stack.append(i)  # 현재 인덱스 추가
    
    # 스택에 남아 있는 인덱스 처리 (끝까지 가격이 안 떨어진 경우)
    while stack:
        prev = stack.pop()
        answer[prev] = n - 1 - prev  # 끝까지의 기간
    
    return answer