from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
m, n = map(int, input().split())  # m: 가로, n: 세로
graph = []  # 토마토 상자 상태 저장

# 토마토 상자 정보 입력
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS에 사용할 큐 생성 및 익은 토마토의 위치를 모두 큐에 추가
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  # 익은 토마토가 있는 경우
            queue.append((i, j))  # 모든 익은 토마토를 시작점으로 추가

# BFS 시작
def bfs():
    while queue:
        x, y = queue.popleft()
        # 상하좌우로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에 있고, 익지 않은 토마토(0)인 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1  # 익은 날짜를 표시 (이전 값 + 1)
                queue.append((nx, ny))  # 다음 탐색 대상으로 추가

# BFS 수행
bfs()

# 결과 확인
max_days = 0
all_ripe = True
for i in range(n):
    for j in range(m):
        # 익지 않은 토마토가 있는 경우
        if graph[i][j] == 0:
            all_ripe = False  # 모두 익을 수 없는 상태
        max_days = max(max_days, graph[i][j])  # 최대로 걸린 날짜 갱신

# 결과 출력
if not all_ripe:
    print(-1)  # 모두 익을 수 없는 경우
elif max_days == 1:
    print(0)  # 처음부터 모두 익은 상태인 경우
else:
    print(max_days - 1)  # 최소 날짜 출력
