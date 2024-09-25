import sys
input = sys.stdin.readline
from collections import deque

# 내가 뽑아낼 숫자가 왼쪽에 있는지, 오른쪽에 있는지 정하여 따로 처리한다.
# 중요한 점은 0번째 인덱스에 오면 뽑아내므로,
# 정중앙에 위치하는 경우에는 왼쪽으로 보내주는게 1 카운트만큼 이득이라는 것을 생각해야 한다.

n, m = map(int, input().split())
queue = deque(i + 1 for i in range(n))  # 1부터 n까지 큐 생성

nums = list(map(int, input().split()))  # 뽑아낼 숫자 리스트

cnt = 0  # 회전 횟수를 저장할 변수
i = 0  # 뽑아야 할 숫자의 인덱스

while i < m:
    if nums[i] == queue[0]:  # 맨 앞에 있는 숫자가 우리가 뽑아야 할 숫자일 때
        queue.popleft()  # 그 숫자를 큐에서 제거
        i += 1  # 다음 숫자로 넘어감
    else:
        mid = len(queue) // 2  # 큐의 중간 인덱스 계산
        target_idx = queue.index(nums[i])  # 뽑아야 할 숫자의 인덱스 찾기
        if target_idx <= mid:  # 뽑아야 할 숫자가 중간보다 앞에 있으면
            queue.append(queue.popleft())  # 왼쪽으로 회전
            cnt += 1
        else:  # 뽑아야 할 숫자가 중간보다 뒤에 있으면
            queue.appendleft(queue.pop())  # 오른쪽으로 회전
            cnt += 1

print(cnt)

