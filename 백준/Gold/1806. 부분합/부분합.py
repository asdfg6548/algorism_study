# 입력을 받음
import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 결과값 초기화 (가장 큰 값으로 설정)
min_length = sys.maxsize
# 두 포인터와 현재 부분합 초기화
start, end = 0, 0
current_sum = 0

# 두 포인터를 이용해 부분합 탐색
while True:
    # 부분합이 S 이상인 경우 최소 길이를 갱신하고 start 포인터를 증가시킴
    if current_sum >= s:
        min_length = min(min_length, end - start)
        current_sum -= arr[start]
        start += 1
    # 부분합이 S 미만인 경우 end 포인터를 증가시켜 부분합을 늘림
    elif end == n:  # end 포인터가 배열 끝에 도달한 경우 종료
        break
    else:
        current_sum += arr[end]
        end += 1

# 최종 결과 출력 (조건을 만족하는 최소 길이 또는 0을 출력)
if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)
