import sys
from collections import deque
input = sys.stdin.readline

# 입력 처리
n = int(input())
grp = [list(input().strip()) for _ in range(n)]

# 단일 방문 배열 (전역)
visited = [[0] * n for _ in range(n)]

# 상하좌우 이동 방향
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def sol_normal(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    color = grp[x][y]
    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0 and color == grp[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

def sol_color_blind(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    color = grp[x][y]
    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0:
                if color == grp[nx][ny] or (color in 'RG' and grp[nx][ny] in 'RG'):
                    visited[nx][ny] = 1
                    q.append((nx, ny))

# 일반인 구역 수
normal_count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            sol_normal(i, j)
            normal_count += 1

# visited 배열 초기화
visited = [[0] * n for _ in range(n)]

# 적록색약 구역 수
color_blind_count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            sol_color_blind(i, j)
            color_blind_count += 1

# 결과 출력
print(normal_count, color_blind_count)