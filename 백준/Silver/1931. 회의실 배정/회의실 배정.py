import sys
input=sys.stdin.readline

# 입력 받기
N = int(input())  # 회의의 수
meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 끝나는 시간을 기준으로, 끝나는 시간이 같다면 시작 시간을 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 회의실을 사용할 수 있는 최대 회의 개수를 찾기
count = 0
end_time = 0  # 마지막으로 선택된 회의의 끝나는 시간

for start, end in meetings:
    if start >= end_time:
        # 현재 회의가 이전 회의의 끝나는 시간 이후에 시작하면 선택
        count += 1
        end_time = end  # 끝나는 시간을 업데이트

# 결과 출력
print(count)