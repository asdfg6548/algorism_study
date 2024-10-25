import sys
input=sys.stdin.readline

n=int(input())
res=[]

for i in range(n):
    inp=list(input().split())

    if inp[1]=='enter':
        res.append(inp[0])
    else:
        res.remove(inp[0])

res.sort(reverse=True)

for i in res:
    print(i)