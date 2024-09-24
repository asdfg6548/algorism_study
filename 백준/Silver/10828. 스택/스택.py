import sys
input=sys.stdin.readline

n=int(input())

res=[]

for i in range(n):
    data=list(input().split())
    if data[0]=="push":
        res.append(data[1])
    elif data[0]=="pop":
        if res:
            print(res.pop())
        else:
            print(-1)
    elif data[0]=="size":
        print(len(res))
    elif data[0]=="empty":
        if res:
            print(0)
        else:
            print(1)
    elif data[0]=="top":
        if res:
            print(res[-1])
        else:
            print(-1)