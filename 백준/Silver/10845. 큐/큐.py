import sys

res = []
n = int(input())

for i in range(n):
    data = list(sys.stdin.readline().split())
    if data[0] == "push":
        res.append(data[1])
    if data[0] == "pop":
        if res:
            print(res.pop(0))
        else:
            print(-1)
    if data[0] == "size":
        print(len(res))
    if data[0] == "empty":
        if res:
            print(0)
        else:
            print(1)
    if data[0] == "front":
        if res:
            print(res[0])
        else:
            print(-1)
    if data[0] == "back":
        if res:
            print(res[-1])
        else:
            print(-1)
