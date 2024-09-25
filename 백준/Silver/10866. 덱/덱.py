import sys
input = sys.stdin.readline
from collections import deque

n=int(input())

res=deque()

for i in range(n):
    inp=list(input().split())
    if inp[0]=="push_front":
        res.appendleft(inp[1])
    elif inp[0]=="push_back":
        res.append(inp[1])
    elif inp[0]=="pop_front":
        if res:
            print(res.popleft())
        else:
            print(-1)
    elif inp[0]=="pop_back":
        if res:
            print(res.pop())
        else:
            print(-1)
    elif inp[0]=="size":
        print(len(res))
    elif inp[0]=="empty":
        if res:
            print(0)
        else:
            print(1)
    elif inp[0]=="front":
        if res:
            print(res[0])
        else:
            print(-1)
    elif inp[0]=="back":
        if res:
            print(res[-1])
        else:
            print(-1)
