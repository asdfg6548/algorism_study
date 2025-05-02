# stack에 큰 것 순서로 남기고 더 없애야하면 뒤에서 부터 제거
def solution(number, k):
    stack = []
    
    for digit in number:
        # 스택의 마지막 숫자가 현재 숫자보다 작고, 제거 횟수가 남아 있다면 제거
        while stack and stack[-1] < digit and k > 0:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # 큰수부터 내림차순으로 정렬
    # 만약 k가 남아 있다면, 뒤에서 k개 제거
    if k > 0:
        stack = stack[:-k]
    
    # 스택을 문자열로 변환하여 반환
    return ''.join(stack)