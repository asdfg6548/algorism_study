from collections import Counter

def solution(topping):
    answer = 0  # 공평한 자르는 방법의 수
    
    # 오른쪽 조각의 토핑 개수를 Counter로 저장
    right_counter = Counter(topping)
    left_counter = {}  # 왼쪽 조각의 토핑 개수
    left_types = 0  # 왼쪽 조각의 고유 토핑 개수
    right_types = len(right_counter)  # 오른쪽 조각의 고유 토핑 개수
    
    # 각 자르는 위치를 순회 (왼쪽에서 하나씩 추가)
    for i in range(len(topping) - 1):  # 마지막은 오른쪽이 빈 경우이므로 제외
        # 현재 토핑을 왼쪽에 추가
        curr = topping[i]
        left_counter[curr] = left_counter.get(curr, 0) + 1
        if left_counter[curr] == 1:  # 새로운 토핑이면
            left_types += 1
        
        # 오른쪽에서 현재 토핑 제거
        right_counter[curr] -= 1
        if right_counter[curr] == 0:  # 토핑이 완전히 제거되면
            right_types -= 1
        
        # 왼쪽과 오른쪽의 고유 토핑 개수가 같으면
        if left_types == right_types:
            answer += 1
    
    return answer