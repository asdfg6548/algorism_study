import sys
input = sys.stdin.readline
from collections import deque

directions=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

def sol(l,start,end):
    def is_valid(x,y):
        return 0 <=x<l and 0<=y<l

    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}

    while queue:
        x,y,steps=queue.popleft()

        if(x,y)==(end[0],end[1]):
            return steps

        for dx,dy in directions:
            nx,ny=x+dx,y+dy

            if is_valid(nx,ny) and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny,steps+1))

    return 0

T = int(input())
for _ in range(T):
    l=int(input())
    start = tuple(map(int, input().split()))  # 시작 위치
    end = tuple(map(int, input().split()))  # 목표 위치
    print(sol(l, start, end))