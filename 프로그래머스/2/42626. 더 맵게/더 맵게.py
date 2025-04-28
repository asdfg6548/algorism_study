import heapq

def solution(scoville, K):
    answer = 0  # 혼합 횟수를 저장하는 변수
    heapq.heapify(scoville)  # 리스트를 최소 힙으로 변환, O(n)

    # 힙의 최소값(첫 번째 요소)이 K 이상이면 혼합이 필요 없음
    if scoville[0] >= K:
        return answer

    # 최소값이 K 미만인 동안 반복
    while scoville[0] < K:
        # 힙에 요소가 1개뿐이면 K 이상으로 만들 수 없음
        if len(scoville) == 1:
            return -1

        # 가장 낮은 스코빌 지수 두 개를 꺼냄
        min_scov = heapq.heappop(scoville)  # 최소값, O(log n)
        min_scov2 = heapq.heappop(scoville)  # 두 번째 최소값, O(log n)

        # 새로운 스코빌 지수 계산: 첫 번째 + 두 번째 * 2
        new_scov = min_scov + min_scov2 * 2
        heapq.heappush(scoville, new_scov)  # 새 값을 힙에 삽입, O(log n)

        answer += 1  # 혼합 횟수 증가

    return answer  # 필요한 최소 혼합 횟수 반환