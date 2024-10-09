from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
cnt=0
res=[]

for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    are=1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny >=m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                are+=1
                queue.append((nx, ny))
    res.append(are)

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:  # 그림이 그려져있다면 BFS 탐색 시작
            bfs(x, y)
            cnt += 1  # 그림 갯수 +1

print(cnt)
print(max(res) if res else 0)  # 가장 큰 영역의 크기 출력 (영역이 없으면 0)