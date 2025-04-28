def solution(order):
    stack = []  # 보조 컨테이너 벨트(스택) 초기화
    n = len(order)  # 상자 개수
    idx = 0  # 현재 실어야 할 order의 인덱스 (실은 상자 개수 추적)
    
    # 컨테이너 벨트에서 1번부터 n번 상자까지 순서대로 처리
    for i in range(1, n + 1):
        stack.append(i)  # 현재 상자(i)를 스택(보조 벨트)에 넣음
        # 스택이 비어 있지 않고, 스택 맨 위 상자가 실어야 할 상자(order[idx])와 같으면
        while stack and stack[-1] == order[idx]:
            stack.pop()  # 스택에서 상자를 꺼내 트럭에 싣음
            idx += 1  # 다음 실어야 할 상자로 이동 (실은 상자 개수 증가)
    
    return idx  # 실은 상자 개수 반환