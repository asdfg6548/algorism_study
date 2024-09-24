import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

for i in range(n):
    inp = list(input().rstrip())
    left = deque()
    right = deque()

    for j in inp:
        if j == '<':
            if left:
                right.appendleft(left.pop())  # 왼쪽에서 뽑아서 오른쪽의 맨 앞에 추가
        elif j == '>':
            if right:
                left.append(right.popleft())  # 오른쪽에서 뽑아서 왼쪽에 추가
        elif j == '-':
            if left:
                left.pop()  # 왼쪽에서 하나 제거
        else:
            left.append(j)  # 일반 문자는 왼쪽에 추가

    print(''.join(left + right))  # left와 right를 합쳐서 출력