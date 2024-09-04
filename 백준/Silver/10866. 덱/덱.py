import sys
from collections import deque

res=deque()
n=int(input())

for i in range(n):
    data = list(sys.stdin.readline().split())
    if data[0]=="push_front":
        res.appendleft(data[1])

    if data[0] == "push_back":
        res.append(data[1])
    
    if data[0]=="pop_front":
        if res:
            print(res.popleft())
        else:
            print(-1)

    if data[0]=="pop_back":
        if res:
            print(res.pop())
        else:
            print(-1)

            
    if data[0]=="size":
        print(len(res))
        
    if data[0]=="empty":
        if res:
            print(0)
        else:
            print(1)
            
    if data[0]=="front":
        if res:
            print(res[0])
        else:
            print(-1)
            
    if data[0]=="back":
        if res:
            print(res[-1])
        else:
            print(-1)