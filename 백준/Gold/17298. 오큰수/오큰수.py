import sys
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))

res=[-1]*n
stack=[]

for i in range(n):
    while stack and data[i]>data[stack[-1]]:
        res[stack[-1]]=data[i]
        stack.pop()
    stack.append(i)
print(*res)