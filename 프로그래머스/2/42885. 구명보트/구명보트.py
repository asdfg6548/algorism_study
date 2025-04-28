# 가장 무거운 사람과 가장 가벼운 사람을 짝지어 태우는 것이 효율적 (그리디)
def solution(people, limit):
    answer = 0  # 필요한 구명보트 개수를 저장
    people.sort()  # 사람들의 몸무게를 오름차순 정렬
    left = 0  # 가장 가벼운 사람의 인덱스 (왼쪽 포인터)
    right = len(people) - 1  # 가장 무거운 사람의 인덱스 (오른쪽 포인터)
    
    while left <= right:  # 두 포인터가 만나거나 교차할 때까지 반복
        # left < right일 때만 두 사람을 태울 가능성 확인
        # 두 사람의 무게 합이 limit 이하면 함께 태움
        if left < right and people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람 태웠으므로 다음 사람으로
        # 무거운 사람은 항상 태움 (혼자 또는 가벼운 사람과 함께)
        right -= 1  # 무거운 사람 태웠으므로 이전 사람으로
        answer += 1  # 보트 한 대 사용
    
    return answer  # 최소 보트 개수 반환