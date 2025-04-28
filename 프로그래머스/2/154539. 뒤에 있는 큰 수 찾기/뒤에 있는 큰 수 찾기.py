def solution(numbers):
    n = len(numbers)
    answer = [-1] * n  # 초기값 -1로 설정
    stack = []  # 인덱스를 저장하는 스택
    
    for i in range(n):
        while stack and numbers[stack[-1]]<numbers[i]:
            answer[stack.pop()]=numbers[i]
        stack.append(i)
    
    return answer