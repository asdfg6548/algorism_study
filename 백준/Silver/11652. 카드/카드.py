from collections import Counter

# 입력 받기
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))

def find_most_common_number(numbers):
    # 숫자의 빈도수를 계산
    count = Counter(numbers)

    # 가장 빈도수가 높은 숫자들을 찾음
    max_count = max(count.values())

    most_common = []
    for num, freq in count.items():
        if freq == max_count:
            most_common.append(num)

    # 가장 빈도수가 높은 숫자 중 가장 작은 값을 반환
    return min(most_common)

# 결과 출력
result = find_most_common_number(cards)
print(result)