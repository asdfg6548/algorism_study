import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
data = deque(i + 1 for i in range(n))

while len(data) > 1:
    data.popleft()
    data.append(data.popleft())

print(*data)
