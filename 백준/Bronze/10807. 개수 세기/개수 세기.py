import sys
input = sys.stdin.readline

n=int(input())
res=0

data=list(map(int,input().split()))
k=int(input())

for i in data:
    if i==k:
        res+=1

print(res)
